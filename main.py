"""
main.py
Entry point — load config, show banner, start the evaluation run.

Usage:
    python main.py
"""
import asyncio

try:
    import config
except ModuleNotFoundError:
    print(
        "\n✗  config.py not found.\n"
        "   Run:  cp config.example.py config.py\n"
        "   Then fill in your credentials.\n"
    )
    raise SystemExit(1)

from core.logger import banner
from workflows.evaluator import run

CONFIG = {
    "USER_ID":     config.USER_ID,
    "PASSWORD":    config.PASSWORD,
    "BASE_URL":    config.BASE_URL,
    "SEM_ID":      config.SEM_ID,
    "COMMENT":     config.COMMENT,
    "RADIO_VALUE": config.RADIO_VALUE,
    "HEADLESS":    config.HEADLESS,
    "DELAY_MS":    config.DELAY_MS,
}

if __name__ == "__main__":
    banner(CONFIG["SEM_ID"], CONFIG["RADIO_VALUE"], CONFIG["COMMENT"])
    asyncio.run(run(CONFIG))
