"""
core/logger.py
Lightweight console logger with consistent prefixes.
"""


def info(msg: str):
    print(f"  {msg}")


def success(msg: str):
    print(f"  ✓ {msg}")


def warn(msg: str):
    print(f"  ⚠ {msg}")


def error(msg: str):
    print(f"  ✗ {msg}")


def section(title: str):
    print(f"\n── {title}")


def banner(sem_id: str, radio_value: str, comment: str):
    print(f"""
╔════════════════════════════════════════════════════════════════════════════════════════╗
║  BAUET Faculty Evaluation Bot v3                                                       ║
║                                                                                        ║
║  Config:                                                                               ║
║    Semester   : {sem_id:<67}║
║    Radio Value: {radio_value:<67}║
║    Comment    : {comment:<67}║
╚════════════════════════════════════════════════════════════════════════════════════════╝
""")
