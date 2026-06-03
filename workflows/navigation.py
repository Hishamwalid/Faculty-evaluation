"""
workflows/navigation.py
Scan the faculty evaluation list and return URLs of PENDING items only.
"""
from selectors.page_selectors import (
    TABLE_ROW,
    PENDING_BADGE,
    START_LINK,
    START_BUTTON,
)


async def get_pending_starts(page, base_url: str) -> list:
    """
    Walk every table row on the faculty list page.
    Returns a list of absolute URLs for pending evaluations.
    '__button__' is appended instead of a URL when the trigger is a JS button.
    """
    try:
        rows = await page.query_selector_all(TABLE_ROW)
        pending_hrefs = []

        for row in rows:
            try:
                pending_badge = await row.query_selector(PENDING_BADGE)
                if not pending_badge:
                    continue

                # Row is pending — grab its Start link or button
                start_link = await row.query_selector(START_LINK)
                if start_link:
                    href = await start_link.get_attribute("href")
                    if href:
                        full = href if href.startswith("http") else base_url + href
                        pending_hrefs.append(full)
                else:
                    start_btn = await row.query_selector(START_BUTTON)
                    if start_btn:
                        pending_hrefs.append("__button__")

            except Exception:
                # Row may lack a status cell — skip cleanly
                continue

        if not pending_hrefs:
            # Fallback: collect all Start links (older iEMS layout compatibility)
            links = await page.query_selector_all(START_LINK)
            for link in links:
                href = await link.get_attribute("href")
                if href:
                    full = href if href.startswith("http") else base_url + href
                    pending_hrefs.append(full)

        return pending_hrefs

    except Exception as e:
        print(f"✗ Error scanning faculty list: {e}")
        return []
