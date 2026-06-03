# Troubleshooting

---

**`python: command not found` on Windows**

Windows maps the Python binary to `py` in many environments.

```bash
py main.py
```

---

**Chromium install fails or permission error (Windows)**

Use `npx` to bypass local policy restrictions:

```bash
npx playwright install chromium
```

---

**Missing `.so` shared library errors (Linux)**

Run the system-dependency installer:

```bash
python3 -m playwright install-deps
```

---

**`config.py not found` error**

Copy the example file and fill in credentials:

```bash
cp config.example.py config.py
```

---

**Login fails immediately**

- Confirm `USER_ID` and `PASSWORD` are correct in `config.py`.
- Try `HEADLESS = False` to watch the browser and see what breaks.
- Increase `DELAY_MS` to `800` if the portal loads slowly.

---

**Radios selected but comment box stays empty**

The Angular fallback handles most cases automatically.  
If still failing, increase `DELAY_MS` — the comment textarea may not be rendered yet.

---

**Script stops after 3 failures**

Check terminal output for the specific error type.  
Common causes: session timeout, network drop, form selector changed.  
Try re-running — the bot will re-authenticate automatically.

---

**All evaluations show as Pending every run**

The submission went through but the portal did not redirect.  
Check `HEADLESS = False` to confirm the submit button fires correctly.
