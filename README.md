# RadarBot

Python scraper that monitors job offers (Welcome to the Jungle, Indeed) and upcoming CTF competitions (CTFtime), then sends real-time Discord notifications based on your keywords and filters.

---

## Features

- Scrapes job offers from **Welcome to the Jungle** and **Indeed**
- Fetches upcoming CTFs from **CTFtime**
- Sends notifications via **Discord webhook**
- Configurable keywords, location, and CTF weight filter
- Runs on a scheduled interval

---

## Project Structure

```
scraper/
├── scrapers/
│   ├── wtj.py          # Welcome to the Jungle scraper
│   ├── indeed.py       # Indeed scraper
│   └── ctftime.py      # CTFtime scraper
├── main.py             # Entry point
├── config.py           # Configuration (keywords, webhook, etc.)
├── notifier.py         # Discord webhook notifications
├── requirements.txt    # Dependencies
└── .gitignore
```

---

## Installation

### Prerequisites

- Python 3.x
- pip3

### Steps

```bash
git clone git@github.com:Jpandreau/RadarBot.git
cd radarbot
pip3 install -r requirements.txt
```

Configure your settings in `config.py` :

```python
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/..."
JOB_KEYWORDS = ["stage", "alternance", "python"]
JOB_LOCATION = "France"
CTF_MIN_WEIGHT = 10
CHECK_INTERVAL_HOURS = 6
```

Run :

```bash
python3 main.py
```

---

## Commit Convention

| Tag | Usage |
|---|---|
| `[ADD]` | New file or feature |
| `[FIX]` | Bug fix |
| `[REM]` | Remove file or feature |
| `[CODINGSTYLE]` | Formatting, naming, style |
| `[REFACTOR]` | Code restructure without behavior change |
| `[DOCS]` | README, comments, documentation |

**Examples :**
```
[ADD] ctftime scraper
[FIX] discord webhook payload format
[REM] unused import in notifier.py
[DOCS] update README installation steps
```

---

## Dependencies

- `requests`
- `beautifulsoup4`
- `lxml`
- `schedule`
