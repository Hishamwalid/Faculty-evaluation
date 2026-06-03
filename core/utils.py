"""
core/utils.py
Shared helpers used across workflow modules.
"""
import asyncio


async def wait_for_angular(page, timeout_ms: int = 10000) -> bool:
    """
    Wait for AngularJS $digest cycle to complete.
    Returns True when Angular is idle, False on timeout or error.
    """
    print("  Waiting for AngularJS to render…")
    try:
        await asyncio.wait_for(
            page.evaluate("""
                new Promise((resolve) => {
                    if (window.angular) {
                        // Angular exists — wait for digest to settle
                        const injector = window.angular.injector(['ng']);
                        const $rootScope = injector.get('$rootScope');

                        if ($rootScope.$$phase) {
                            // Still in a digest cycle — watch until it clears
                            $rootScope.$watch(() => {
                                if (!$rootScope.$$phase) resolve();
                            });
                        } else {
                            resolve();
                        }
                    } else {
                        // No Angular on this page — proceed immediately
                        resolve();
                    }
                });
            """),
            timeout=timeout_ms / 1000,
        )
        print("  ✓ Angular ready")
        return True
    except asyncio.TimeoutError:
        print("  ⚠ Angular load timeout (continuing anyway)")
        return False
    except Exception as e:
        print(f"  ⚠ Angular wait error: {type(e).__name__}")
        return False
