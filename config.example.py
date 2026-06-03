# ─────────────────────────────────────────────────────────────
#  config.example.py
#  Copy this file:  cp config.example.py config.py
#  Then fill in your credentials below.
#  config.py is listed in .gitignore — your data stays private.
# ─────────────────────────────────────────────────────────────

# Portal credentials
USER_ID  = "YOUR_STUDENT_ID"       # e.g. "2021xxxx"
PASSWORD = "YOUR_PORTAL_PASSWORD"

# Target portal URL (do not add trailing slash)
BASE_URL = "https://iems.bauet.ac.bd"

# Semester ID — see README § "How to Find Your SEM_ID"
# Convention: ends in 01 = Summer, 02 = Winter  (e.g. "202502")
SEM_ID = "202502"

# Text typed into the evaluation comment box
COMMENT = "Good"

# Likert scale rating submitted for every radio group:
#   "1" = Strongly Agree / Outstanding
#   "2" = Agree        / Very Good
#   "3" = Neutral      / Good
#   "4" = Disagree     / Poor
#   "5" = Strongly Disagree / Very Poor
RADIO_VALUE = "3"

# Set True to run browser invisibly (no visible window)
HEADLESS = False

# Milliseconds to pause between key actions (increase on slow connections)
DELAY_MS = 500
