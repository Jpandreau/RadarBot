import json
import os
import schedule
import time

from config import CHECK_INTERVAL_HOURS
from notifier import notify_job
from scrapers.wtj import fetch_wtj_jobs
from scrapers.hellowork import fetch_hellowork_jobs

SEEN_FILE = os.path.join(os.getenv("DATA_DIR", "."), "seen_jobs.json")


def load_seen() -> set:
    if not os.path.exists(SEEN_FILE):
        return set()
    with open(SEEN_FILE, "r") as f:
        return set(json.load(f))


def save_seen(seen: set):
    with open(SEEN_FILE, "w") as f:
        json.dump(list(seen), f)


def check_jobs():
    print("Vérification des offres...")
    seen = load_seen()
    new_seen = set()

    jobs = fetch_wtj_jobs() + fetch_hellowork_jobs()

    for job in jobs:
        job_id = job["id"]
        if job_id not in seen:
            notify_job(job)
            new_seen.add(job_id)
            time.sleep(2)

    seen.update(new_seen)
    save_seen(seen)
    print(f"{len(new_seen)} nouvelle(s) offre(s) notifiée(s).")


if __name__ == "__main__":
    check_jobs()
    schedule.every(CHECK_INTERVAL_HOURS).hours.do(check_jobs)

    while True:
        schedule.run_pending()
        time.sleep(60)
