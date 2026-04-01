# RadarBot

Python scraper that monitors IT job offers from Welcome to the Jungle and Hellowork, then sends real-time Discord notifications based on keywords and a geographic radius filter.

---

## Features

- Scrapes job offers from **Welcome to the Jungle** (via Algolia API) and **Hellowork** (HTML parsing)
- Filters IT-related jobs only (regex on title)
- Geographic filter: **200km radius around Moulins (03)**
- Sends notifications via **Discord webhook** (embedded messages)
- Deduplication via `seen_jobs.json` — no double notifications
- Runs every **6 hours** on a scheduled interval

---

## Project Structure

```
RadarBot/
├── scrapers/
│   ├── wtj.py          # Welcome to the Jungle scraper (Algolia API)
│   └── hellowork.py    # Hellowork scraper (BeautifulSoup)
├── main.py             # Entry point + deduplication loop
├── config.py           # Configuration (keywords, location, interval)
├── notifier.py         # Discord webhook notifications
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image
├── docker-compose.yml  # Docker Compose deployment
├── .env.example        # Environment variable template
└── .gitignore
```

---

## Configuration

Copy `.env.example` to `.env` and fill in your Discord webhook URL:

```
webhook=https://discord.com/api/webhooks/XXXXXXXX/XXXXXXXX
```

Keywords and location are configured in `config.py`:

```python
JOB_KEYWORDS = [
    "stage informatique",
    "stage développeur",
    "stage data",
    "stage cybersécurité",
    "stage réseau",
]
JOB_LOCATION = "Moulins, Allier"
JOB_RADIUS_KM = 200
CHECK_INTERVAL_HOURS = 6
```

---

## Deployment

### Docker (recommended — no Python required)

```bash
git clone git@github.com:Jpandreau/RadarBot.git
cd RadarBot
cp .env.example .env
# Edit .env with your Discord webhook URL
docker compose up -d --build
```

View logs:
```bash
docker compose logs -f
```

Stop:
```bash
docker compose down
```

### Manual (Python 3.12+)

```bash
git clone git@github.com:Jpandreau/RadarBot.git
cd RadarBot
pip3 install -r requirements.txt
cp .env.example .env
# Edit .env with your Discord webhook URL
python3 main.py
```

---

## Dependencies

- `requests`
- `beautifulsoup4`
- `lxml`
- `python-dotenv`
- `schedule`

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

**Examples:**
```
[ADD] hellowork scraper with IT keyword filter
[FIX] discord webhook 429 rate limit with sleep between notifications
[DOCS] update README with Docker deployment instructions
```
