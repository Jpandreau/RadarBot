import requests
from config import DISCORD_WEBHOOK_URL

def notify_job(job):
    data = {
        "embeds": [{
            "title": job["title"],
            "description": job["company"],
            "color": 0x57F287,
            "fields": [
                {"name": "Lieu", "value": job["location"], "inline": True},
                {"name": "Lien", "value": job["url"], "inline": False},
            ]
        }]
    }
    requests.post(DISCORD_WEBHOOK_URL, json=data).raise_for_status()
