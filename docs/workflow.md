# Workflow Reference

```
CONFIG → main.py → evaluator.py
                      │
                      ├── login.py          (authenticate)
                      ├── navigation.py     (scan pending list)
                      └── form_handler.py   (fill + submit)
                              │
                              ├── core/utils.py    (wait_for_angular)
                              ├── core/browser.py  (crash recovery)
                              └── selectors/*.py   (all CSS selectors)
```

## Step-by-step

| Step | Module                    | Action                                      |
|------|---------------------------|---------------------------------------------|
| 1    | `main.py`                 | Load config, show banner                    |
| 2    | `core/browser.py`         | Launch Chromium, open page                  |
| 3    | `workflows/login.py`      | Fill credentials, verify redirect           |
| 4    | `workflows/navigation.py` | Scan table, collect Pending URLs            |
| 5    | `workflows/form_handler.py`| Open form, select radios, type comment     |
| 6    | `workflows/form_handler.py`| Validate, submit                           |
| 7    | `workflows/evaluator.py`  | Loop back to step 4 until list is empty     |
| 8    | `workflows/evaluator.py`  | Print summary, close browser                |

## Retry logic

- Up to `3` consecutive failures before aborting.
- Page closed mid-run → new page opened, re-login attempted.
- Full browser crash → new browser launched, re-login attempted.
