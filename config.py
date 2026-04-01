from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_WEBHOOK_URL = os.getenv("webhook")
JOB_KEYWORDS = {
    "Développement": ["stage développeur", "stage informatique"],
    "Cybersécurité": ["stage cybersécurité"],
    "Réseau": ["stage réseau"],
    "Data": ["stage data"],
}
JOB_LOCATION = "Moulins, Allier"
JOB_LAT = 46.5647
JOB_LNG = 3.3322
JOB_RADIUS_KM = 200
CHECK_INTERVAL_HOURS = 6