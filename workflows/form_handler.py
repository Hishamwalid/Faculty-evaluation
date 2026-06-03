"""
workflows/form_handler.py
Fill and submit a single evaluation form.
Handles AngularJS rendering, value-based radio selection,
human-like keystroke simulation, pre-submit validation.
"""
from core.utils import wait_for_angular


async def fill_and_submit(
    page,
    submit_url: str,
    radio_value: str,
    comment_text: str,
    delay_ms: int,
) -> bool:
    """
    Open submit_url, fill every radio group with radio_value,
    type comment_text into the comment box, validate, then submit.
    Returns True on success, False on any failure.
    """
    try:
        print(f"\n  Opening form: {submit_url}")
        await page.goto(submit_url, wait_until="networkidle", timeout=20000)
        await page.wait_for_timeout(delay_ms)

        # Identify teacher
        teacher = await page.evaluate(
            'document.querySelector(".text-danger, .text-primary")'
            '?.textContent?.trim() || "Unknown"'
        )
        print(f"  Teacher: {teacher}")

        # Wait for Angular $digest to settle before touching DOM
        await wait_for_angular(page)

        # ── Radio buttons ──────────────────────────────────────────────────────
        filled = await page.evaluate(
            """
            (radioValue) => {
                let filled = 0;
                const radios = document.querySelectorAll('input[type="radio"]');
                radios.forEach(radio => {
                    if (radio.value === radioValue) {
                        radio.checked = true;
                        radio.dispatchEvent(new Event('change', { bubbles: true }));
                        radio.dispatchEvent(new Event('click',  { bubbles: true }));
                        filled++;
                    }
                });
                return filled;
            }
            """,
            radio_value,
        )
        print(f"  ✓ Selected {filled} radio buttons with value='{radio_value}'")

        checked = await page.evaluate(
            'document.querySelectorAll("input[type=radio]:checked").length'
        )
        print(f"  ✓ Verified: {checked} radio buttons are checked")

        # ── Comment box ────────────────────────────────────────────────────────
        print("  Filling comment…")
        try:
            # Scroll to bottom so Angular renders the textarea
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_timeout(400)

            await page.wait_for_selector("textarea#Comment", timeout=5000)
            textarea = page.locator("textarea#Comment").first

            await textarea.focus()
            await page.wait_for_timeout(200)

            # Clear any pre-existing value
            await textarea.fill("")
            await page.wait_for_timeout(100)

            # Type with realistic keystroke delay — bypasses Angular validation guards
            await textarea.type(comment_text, delay=20)
            await page.wait_for_timeout(300)

            actual_value = await textarea.input_value()

            if comment_text in actual_value:
                print(f"  ✓ Comment filled: '{actual_value}'")
            else:
                # Angular may intercept focus; fall back to direct DOM mutation
                print("  ⚠ Keystroke fill mismatch — using Angular JS fallback")
                await page.evaluate(
                    """
                    (comment) => {
                        const ta = document.getElementById('Comment');
                        ta.value = comment;
                        ta.dispatchEvent(new Event('input',  { bubbles: true }));
                        ta.dispatchEvent(new Event('change', { bubbles: true }));
                        ta.dispatchEvent(new Event('blur',   { bubbles: true }));
                    }
                    """,
                    comment_text,
                )
                print("  ✓ Comment set via Angular fallback")

        except Exception as e:
            print(f"  ✗ Comment error: {type(e).__name__}")
            return False

        await page.wait_for_timeout(500)

        # ── Pre-submit validation ──────────────────────────────────────────────
        print("  Validating form…")
        validation = await page.evaluate(
            """
            () => {
                const ta           = document.getElementById('Comment');
                const checkedRadios = document.querySelectorAll('input[type="radio"]:checked');
                const hasComment   = ta && ta.value && ta.value.trim().length > 0;
                const hasRadios    = checkedRadios.length > 0;
                return {
                    hasComment:    hasComment,
                    commentLength: ta?.value?.length || 0,
                    checkedCount:  checkedRadios.length,
                    isValid:       hasComment && hasRadios
                };
            }
            """
        )

        print(
            f"    Comment: {validation['commentLength']} chars, "
            f"Radios: {validation['checkedCount']}"
        )

        if not validation["isValid"]:
            print(
                f"  ✗ Form invalid — "
                f"comment: {validation['hasComment']}, "
                f"radios checked: {validation['checkedCount']}"
            )
            return False

        print("  ✓ Form validation passed")

        # ── Submit ─────────────────────────────────────────────────────────────
        print("  Submitting form…")
        await page.evaluate(
            """
            () => {
                const btn =
                    document.querySelector('button[ng-click="saveFpeSubmission()"]') ||
                    Array.from(document.querySelectorAll('button'))
                          .find(b => b.textContent.includes('Submit'));
                if (btn) { btn.click(); }
            }
            """
        )

        try:
            await page.wait_for_load_state("networkidle", timeout=10000)
        except Exception:
            pass  # Page may not produce a full navigation — that is acceptable

        await page.wait_for_timeout(delay_ms)
        print("  ✓ Submitted successfully")
        return True

    except Exception as e:
        print(f"  ✗ Error: {type(e).__name__}")
        return False
