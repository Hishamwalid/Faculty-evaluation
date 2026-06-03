"""
core/browser.py
Launch Playwright Chromium and return a ready (browser, context, page) triple.
"""


async def new_page(pw, headless: bool = False):
    """
    Launch Chromium with a fresh context.
    Returns (browser, context, page).

    Usage:
        async with async_playwright() as p:
            browser, context, page = await new_page(p, headless=False)
    """
    browser = await pw.chromium.launch(headless=headless)
    context = await browser.new_context()
    page    = await context.new_page()
    return browser, context, page
