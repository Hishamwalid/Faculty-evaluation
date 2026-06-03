# BAUET Faculty Evaluation Bot

This tool automatically fills and submits every teacher evaluation on the BAUET iEMS portal for you. You just run it once and it handles everything — logging in, opening each form, selecting ratings, typing your comment, and submitting.

---

## Before You Start — What You Need

You need two things installed on your PC before anything else:

1. **Python** — the language this bot is written in
2. **The project files** — downloaded from this page

Both are free. Both take about 5 minutes. Follow the steps below exactly.

---

## PART 1 — Install Python on Your PC

> Skip this part if you already have Python installed.

### Windows

1. Go to this website: **https://www.python.org/downloads/**
2. Click the big yellow button that says **Download Python**
3. A file like `python-3.x.x.exe` will download — open it
4. **⚠️ Very important:** On the first screen you will see a small checkbox at the bottom that says **"Add Python to PATH"**. **Tick that box before clicking anything else.** If you miss this, nothing will work.
5. Click **Install Now** and wait for it to finish
6. Click **Close** when done

**Check it worked:** Press `Win + R` on your keyboard, type `cmd`, press Enter. A black window opens. Type this and press Enter:
```
python --version
```
You should see something like `Python 3.11.4`. If you see a version number, Python is installed. ✅

---

### macOS

1. Go to **https://www.python.org/downloads/**
2. Click the big yellow **Download Python** button
3. Open the downloaded `.pkg` file and follow the installer steps
4. Click through all the screens and click **Install**

**Check it worked:** Press `Cmd + Space`, type `Terminal`, press Enter. Type this and press Enter:
```
python3 --version
```
You should see a version number. ✅

---

### Linux

Open a terminal (`Ctrl + Alt + T`) and run:
```
sudo apt update && sudo apt install python3 python3-pip -y
```

---

## PART 2 — Download This Project to Your PC

You do not need to know anything about GitHub or Git for this step. Just follow along.

1. Look at the top of this GitHub page
2. Find the green button that says **`<> Code`** — it is near the top right of the file list
3. Click it — a small box will appear
4. Click **Download ZIP** at the bottom of that box
5. A file called `bauet-playwright-automation-main.zip` will download to your **Downloads** folder

**Now extract it:**

- **Windows:** Go to your Downloads folder. Right-click the ZIP file. Click **"Extract All"**. Click **Extract**. A new folder called `bauet-playwright-automation-main` will appear.
- **macOS:** Go to Downloads. Double-click the ZIP file. A folder appears next to it.

You now have the project folder on your PC. ✅

---

## PART 3 — Open a Terminal Inside the Project Folder

This is the step most beginners get confused about. The terminal needs to be "looking at" the project folder. Here is exactly how to do it.

### Windows

1. Open the folder you just extracted (`bauet-playwright-automation-main`)
2. You will see files like `main.py`, `requirements.txt`, etc.
3. Click on the **address bar** at the very top of the window (the bar that shows the folder path like `C:\Users\...`)
4. The path text will get selected/highlighted
5. Type `cmd` (it will replace the highlighted text) and press **Enter**
6. A black Command Prompt window opens — it is already inside the project folder ✅

### macOS

1. Open **Terminal** (`Cmd + Space` → type Terminal → Enter)
2. Type `cd ` (the letters c, d, and a space — **do not press Enter yet**)
3. Open Finder, find the extracted folder, and **drag and drop the folder** into the Terminal window
4. The folder path will appear after `cd `
5. Now press **Enter**

### Linux

1. Open Terminal (`Ctrl + Alt + T`)
2. Type `cd ` then drag the project folder into the terminal, then press Enter

**How to check you are in the right place:**

Type `ls` (macOS/Linux) or `dir` (Windows) and press Enter.
You should see a list that includes `main.py` and `requirements.txt`.
If you see those files, you are in the right place. ✅

---

## PART 4 — Install the Bot's Dependencies

The bot needs one library called Playwright. Install it by copy-pasting this command into your terminal and pressing Enter.

### Windows
```
pip install -r requirements.txt
```

### macOS / Linux
```
pip3 install -r requirements.txt
```

A lot of text will scroll past — that is normal. Wait until it stops and you see the `>` or `$` prompt again.

Then install the browser the bot will use:

### Windows
```
python -m playwright install chromium
```

### macOS / Linux
```
python3 -m playwright install chromium
```

### Linux only — one extra command
```
python3 -m playwright install-deps
```

---

## PART 5 — Enter Your Credentials (Config File)

The bot needs your student ID, password, and semester ID. You enter these in a file called `config.py`. Here is how to create it.

### Step A — Copy the template file

This creates your `config.py` from the example.

**Windows — paste this in your Command Prompt and press Enter:**
```
copy config.example.py config.py
```

**macOS / Linux — paste this in your Terminal and press Enter:**
```
cp config.example.py config.py
```

### Step B — Open config.py and fill in your details

1. Go to the project folder in File Explorer (Windows) or Finder (macOS)
2. Find the file called `config.py`
3. Right-click it → **Open with** → choose **Notepad** (Windows) or **TextEdit** (macOS)

You will see this text:

```python
USER_ID  = "YOUR_STUDENT_ID"
PASSWORD = "YOUR_PORTAL_PASSWORD"
BASE_URL = "https://iems.bauet.ac.bd"
SEM_ID   = "202502"
COMMENT  = "Good"
RADIO_VALUE = "3"
HEADLESS = False
DELAY_MS = 500
```

**Replace the values:**

| What to change | Example |
|---|---|
| `YOUR_STUDENT_ID` | `"2021234"` |
| `YOUR_PORTAL_PASSWORD` | `"mypassword123"` |
| `SEM_ID` | `"202502"` — see below how to find yours |
| `COMMENT` | `"Good"` — whatever comment you want |
| `RADIO_VALUE` | `"3"` — see the rating table below |

> ⚠️ Keep the quote marks `" "` around every value. Only change what is inside them.

**Save the file** — press `Ctrl + S` (Windows) or `Cmd + S` (macOS).

---

### How to Find Your SEM_ID

1. Open your browser and go to **https://iems.bauet.ac.bd**
2. Log in with your student ID and password
3. In the menu on the left, click **Faculty Evaluation**
4. Click the **Start** button next to any teacher
5. Look at the address bar at the top of your browser — the URL will look like this:
   ```
   https://iems.bauet.ac.bd/Student/FacultyEvaluation/FacultyList?semId=202502
   ```
6. The number at the very end after `semId=` is your SEM_ID. Copy that number.
7. Paste it into `config.py` between the quote marks for `SEM_ID`

---

### Rating Guide (RADIO_VALUE)

Pick the number that matches the rating you want to give every teacher:

| Put this in config.py | What it means |
|---|---|
| `"1"` | Strongly Agree / Outstanding |
| `"2"` | Agree / Very Good |
| `"3"` | Neutral / Good |
| `"4"` | Disagree / Poor |
| `"5"` | Strongly Disagree / Very Poor |

---

## PART 6 — Run the Bot

Go back to your terminal (the black window from Part 3) and type:

### Windows
```
python main.py
```

> If you get an error saying `python is not recognized`, try this instead:
> ```
> py main.py
> ```

### macOS / Linux
```
python3 main.py
```

A browser window will open, log in automatically, and start filling each evaluation form one by one. You will see progress in the terminal:

```
→ Logging in …
✓ Logged in

── Round 1: Faculty list …
   Found 3 pending — processing…

  Teacher: Dr. Example
  ✓ Selected 8 radio buttons
  ✓ Comment filled: 'Good'
  ✓ Submitted successfully

🎉 Done! Submitted 3 evaluation(s).
```

Do not close the terminal or the browser while it is running. When it prints `Done!` it is finished.

---

## Something Went Wrong?

| What you see | What to do |
|---|---|
| `python is not recognized` (Windows) | Use `py main.py` instead |
| `pip is not recognized` | You missed the "Add Python to PATH" step — reinstall Python and tick that box |
| `config.py not found` | You skipped Part 5 Step A — run the `copy` or `cp` command |
| `ModuleNotFoundError: playwright` | Run the `pip install` command from Part 4 again |
| Browser opens but login fails | Check your `USER_ID` and `PASSWORD` in `config.py` |
| Bot submits but portal still shows Pending | Wait a minute and run again — the portal sometimes delays refreshing |

Full troubleshooting guide: [`docs/troubleshooting.md`](docs/troubleshooting.md)

---

## Disclaimer

This project is for personal educational purposes only. Use responsibly.

---

## License

[MIT](LICENSE)
