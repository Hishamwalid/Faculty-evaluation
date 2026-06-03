# Setup Guide

## Prerequisites

- Python 3.8+
- pip

---

## Installation

### 1 — Clone

```bash
git clone https://github.com/YOUR_USERNAME/bauet-playwright-automation.git
cd bauet-playwright-automation
```

### 2 — Install Python package

```bash
pip install -r requirements.txt
```

### 3 — Install Chromium binary

**Windows**
```bash
npx playwright install chromium
```

**macOS**
```bash
python3 -m playwright install chromium
```

**Linux**
```bash
python3 -m playwright install chromium
python3 -m playwright install-deps
```

### 4 — Create config

```bash
cp config.example.py config.py
```

Edit `config.py` and fill in `USER_ID`, `PASSWORD`, `SEM_ID`.  
See `data/notes.md` for how to find `SEM_ID`.

---

## Run

```bash
python main.py
```

Windows alternative if `python` is not mapped:
```bash
py main.py
```
