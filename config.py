from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_WEBHOOK_URL = os.getenv("webhook")
JOB_KEYWORDS = [
    "stage informatique",
    "stage développeur",
    "stage data",
    "stage cybersécurité",
    "stage réseau",
]
JOB_LOCATION = "Moulins, Allier"
JOB_LAT = 46.5647
JOB_LNG = 3.3322
JOB_RADIUS_KM = 200
CHECK_INTERVAL_HOURS = 6