import requests
from config import DISCORD_WEBHOOK_URL

CATEGORY_COLORS = {
    "Développement": 0x57F287,
    "Cybersécurité": 0xED4245,
    "Réseau": 0x5865F2,
    "Data": 0x9B59B6,
}

def notify_job(job):
    category = job.get("category", "")
    color = CATEGORY_COLORS.get(category, 0x95A5A6)

    data = {
        "embeds": [{
            "title": job["title"],
            "url": job["url"],
            "description": job["company"],
            "color": color,
            "fields": [
                {"name": "Lieu", "value": job["location"], "inline": True},
                {"name": "Catégorie", "value": category, "inline": True},
            ],
            "footer": {"text": f"via {job['source']}"},
        }]
    }
    requests.post(DISCORD_WEBHOOK_URL, json=data).raise_for_status()
