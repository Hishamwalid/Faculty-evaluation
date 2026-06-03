"""
workflows/evaluator.py
Main workflow controller — the "brain".
Loops through pending evaluations, handles retries and crash recovery.
"""
from playwright.async_api import async_playwright

from core.browser import new_page
from workflows.login import login
from workflows.navigation import get_pending_starts
from workflows.form_handler import fill_and_submit


async def run(config: dict):
    """
    Entry point for the full evaluation run.

    config keys:
        USER_ID, PASSWORD, BASE_URL, SEM_ID,
        COMMENT, RADIO_VALUE, HEADLESS, DELAY_MS
    """
    base_url    = config["BASE_URL"]
    sem_id      = config["SEM_ID"]
    user_id     = config["USER_ID"]
    password    = config["PASSWORD"]
    comment     = config["COMMENT"]
    radio_value = config["RADIO_VALUE"]
    headless    = config["HEADLESS"]
    delay_ms    = config["DELAY_MS"]

    list_url = (
        f"{base_url}/Student/FacultyEvaluation/FacultyList?semId={sem_id}"
    )

    async with async_playwright() as p:
        browser, context, page = await new_page(p, headless)

        try:
            # ── Initial login ──────────────────────────────────────────────────
            if not await login(page, base_url, user_id, password, delay_ms):
                return

            total               = 0
            round_              = 0
            consecutive_failures = 0
            max_failures        = 3

            # ── Main loop ──────────────────────────────────────────────────────
            while consecutive_failures < max_failures:
                round_ += 1
                print(f"── Round {round_}: Faculty list …")

                try:
                    # Recover from a closed page
                    if page.is_closed():
                        print("   ⚠ Page closed — reconnecting…")
                        page = await context.new_page()
                        if not await login(page, base_url, user_id, password, delay_ms):
                            break

                    await page.goto(list_url, wait_until="networkidle", timeout=20000)
                    await page.wait_for_timeout(delay_ms)

                    hrefs = await get_pending_starts(page, base_url)

                    if not hrefs:
                        print(f"\n🎉 Done! Submitted {total} evaluation(s).")
                        break

                    print(f"   Found {len(hrefs)} pending — processing…\n")

                    url = hrefs[0]

                    if url == "__button__":
                        # Trigger is a JS button, not a link
                        btn = await page.query_selector('button:has-text("Start")')
                        if btn:
                            await btn.click()
                            await page.wait_for_load_state("networkidle")
                        success = await fill_and_submit(
                            page, page.url, radio_value, comment, delay_ms
                        )
                    else:
                        success = await fill_and_submit(
                            page, url, radio_value, comment, delay_ms
                        )

                    if success:
                        total += 1
                        consecutive_failures = 0
                        # Brief pause between submissions — avoids server strain
                        await page.wait_for_timeout(1000)
                    else:
                        consecutive_failures += 1

                except Exception as e:
                    err = str(e)
                    if "closed" in err.lower():
                        # Full browser crash — rebuild from scratch
                        print("   ⚠ Browser closed unexpectedly — restarting…")
                        try:
                            await browser.close()
                        except Exception:
                            pass
                        browser, context, page = await new_page(p, headless)
                        if not await login(page, base_url, user_id, password, delay_ms):
                            break
                    else:
                        print(f"   ✗ Round error: {type(e).__name__}\n")

                    consecutive_failures += 1
                    await page.wait_for_timeout(500)

            # ── Final summary ──────────────────────────────────────────────────
            if consecutive_failures >= max_failures:
                print(f"⚠ {max_failures} consecutive failures — stopping.")

            print(f"\n{'=' * 50}")
            print(f"Final: {total} evaluation(s) completed")
            print(f"{'=' * 50}\n")

        except Exception as e:
            print(f"✗ Critical error: {type(e).__name__}: {e}")

        finally:
            print("Closing browser…")
            try:
                await browser.close()
            except Exception:
                pass
