# BAUET Faculty Evaluation Bot (AngularJS Fix v3)

An automated Python script built with **Playwright** that completes the mandatory Faculty Performance Evaluation (FPE) on the BAUET iEMS portal.

The manual evaluation process can be repetitive and time-consuming. This bot automates the workflow by logging in, navigating evaluation forms, selecting ratings, entering comments, and submitting evaluations automatically.

---

## Features

- **AngularJS Form Synchronization** – Handles asynchronous AngularJS rendering without timing out.
- **Reliable Radio Selection** – Uses JavaScript event dispatching to ensure rating selections are properly registered.
- **Human-like Typing Simulation** – Mimics natural typing behavior when filling comments.
- **Pending Form Detection** – Automatically processes only pending evaluations and skips completed ones.
- **Session Recovery** – Re-authenticates and resumes operation if the session is interrupted.

---

## Configuration

Before running the script, update the configuration variables near the top of the file:

```python
# CONFIG
USER_ID = "YOUR_STUDENT_ID"
PASSWORD = "YOUR_PORTAL_PASSWORD"
BASE_URL = "https://iems.bauet.ac.bd"
SEM_ID = "YOUR_SEMESTER_ID"      # Example: "202502"
COMMENT = "Good"                 # Comment submitted with evaluation
RADIO_VALUE = "3"                # Rating value (1-5)
```

### Finding Your `SEM_ID`

1. Log in to the BAUET iEMS Portal.
2. Navigate to **Faculty Evaluation**.
3. Click **Start** for the current evaluation period.
4. Check the URL in your browser:

```text
https://iems.bauet.ac.bd/Student/FacultyEvaluation/FacultyList?semId=202502
```

5. Copy the value after `semId=`.

### Semester Code Format

| Ending | Semester |
|----------|----------|
| `01` | Summer Semester |
| `02` | Winter Semester |

Examples:

- `202501` → Summer 2025
- `202502` → Winter 2025

---

## Rating Reference

| Value | Description |
|---------|-------------|
| `1` | Strongly Disagree / Very Poor |
| `2` | Disagree / Poor |
| `3` | Neutral / Good |
| `4` | Agree / Very Good |
| `5` | Strongly Agree / Outstanding |

---

# Installation & Usage

Choose the instructions for your operating system.

---

## Windows

### 1. Install Playwright

```bash
pip install playwright
```

### 2. Install Chromium Browser

```bash
npx playwright install chromium
```

### 3. Run the Script

```bash
py your_script_name.py
```

---

## macOS

### 1. Install Playwright

```bash
pip3 install playwright
```

### 2. Install Chromium Browser

```bash
python3 -m playwright install chromium
```

### 3. Run the Script

```bash
python3 your_script_name.py
```

---

## Linux

### 1. Install Playwright

```bash
pip3 install playwright
```

### 2. Install Chromium & System Dependencies

```bash
python3 -m playwright install chromium
python3 -m playwright install-deps
```

### 3. Run the Script

```bash
python3 your_script_name.py
```

---

## Troubleshooting

### Python Command Not Found (Windows)

If:

```bash
python filename.py
```

does not work, try:

```bash
py filename.py
```

Windows often maps Python through the `py` launcher.

---

### Chromium Installation Fails

Use:

```bash
npx playwright install chromium
```

This frequently bypasses local execution policy restrictions.

---

### Linux Shared Library Errors

If Playwright reports missing `.so` libraries:

```bash
python3 -m playwright install-deps
```

This installs the required system packages.

---

## Disclaimer

This project is intended for educational and personal productivity purposes only.

Use responsibly and ensure that any automated interactions comply with your institution's policies. If your script includes configurable delays (e.g., `DELAY_MS`), consider using them to avoid generating excessive load on university infrastructure.

---

## License

This project is provided as-is without warranty. Use at your own risk.
