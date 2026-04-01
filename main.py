import json
import os
import schedule
import time

from config import (
    ALTERNANCE_REQUIRED_TERMS,
    CHECK_INTERVAL_HOURS,
    EXCLUDED_JOB_TERMS,
    JOB_SOURCES,
    validate_config,
)
from notifier import notify_job
from scrapers.hellowork import fetch_hellowork_jobs
from scrapers.linkedin import fetch_linkedin_jobs
from scrapers.wtj import fetch_wtj_jobs

SEEN_FILE = os.path.join(os.getenv("DATA_DIR", "."), "seen_jobs.json")


def load_seen() -> set:
    if not os.path.exists(SEEN_FILE):
        return set()
    with open(SEEN_FILE, "r") as f:
        return set(json.load(f))


def save_seen(seen: set):
    with open(SEEN_FILE, "w") as f:
        json.dump(list(seen), f)


def passes_contract_filter(job: dict) -> bool:
    title = job["title"].lower()
    has_required = any(term in title for term in ALTERNANCE_REQUIRED_TERMS)
    has_excluded = any(term in title for term in EXCLUDED_JOB_TERMS)
    return has_required and not has_excluded


def check_jobs():
    print("Vérification des offres...")
    seen = load_seen()
    new_seen = set()

    jobs = []
    selected = {s.lower() for s in JOB_SOURCES}
    supported = {"wtj", "hellowork", "linkedin"}
    unknown = sorted(selected - supported)

    if unknown:
        print(f"Sources non supportées ignorées : {', '.join(unknown)}")

    if "wtj" in selected:
        jobs.extend(fetch_wtj_jobs())
    if "hellowork" in selected:
        jobs.extend(fetch_hellowork_jobs())
    if "linkedin" in selected:
        jobs.extend(fetch_linkedin_jobs())

    for job in jobs:
        job_id = job.get("id")
        if not job_id:
            continue
        if job_id in seen or job_id in new_seen:
            continue
        if not passes_contract_filter(job):
            continue

        notify_job(job)
        new_seen.add(job_id)
        time.sleep(2)

    seen.update(new_seen)
    save_seen(seen)
    print(f"{len(new_seen)} nouvelle(s) offre(s) notifiée(s).")


if __name__ == "__main__":
    validate_config()
    check_jobs()
    schedule.every(CHECK_INTERVAL_HOURS).hours.do(check_jobs)

    while True:
        schedule.run_pending()
        time.sleep(60)
