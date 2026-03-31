from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_WEBHOOK_URL = os.getenv("webhook")
JOB_KEYWORDS = ["stage", "informatique"]
JOB_LOCATION = "France"
OB_SOURCES = ["wtj", "indeed"]
CHECK_INTERVAL_HOURS = 6