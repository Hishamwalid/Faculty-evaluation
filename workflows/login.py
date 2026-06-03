"""
workflows/login.py
Authentication only — no other logic lives here.
"""
from selectors.login_selectors import (
    USER_ID_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    POST_LOGIN_URL_GLOB,
)


async def login(page, base_url: str, user_id: str, password: str, delay_ms: int) -> bool:
    """
    Navigate to portal, fill credentials, submit, verify redirect.
    Returns True on success, False on any failure.
    """
    print("→ Logging in …")
    try:
        await page.goto(base_url + "/", wait_until="networkidle")
        await page.wait_for_selector(USER_ID_INPUT, timeout=15000)
        await page.fill(USER_ID_INPUT, user_id)
        await page.fill(PASSWORD_INPUT, password)
        await page.wait_for_timeout(delay_ms)
        await page.click(LOGIN_BUTTON)
        await page.wait_for_url(POST_LOGIN_URL_GLOB, timeout=20000)
        print("✓ Logged in\n")
        return True
    except Exception as e:
        print(f"✗ Login failed: {e}")
        return False
