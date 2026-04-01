import requests
from bs4 import BeautifulSoup
from config import JOB_KEYWORDS, JOB_LOCATION, LINKEDIN_MAX_PAGES

SEARCH_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0"
}


def fetch_linkedin_jobs() -> list[dict]:
    results = []
    seen_ids: set[str] = set()

    for category, keywords in JOB_KEYWORDS.items():
        for keyword in keywords:
            for page in range(LINKEDIN_MAX_PAGES):
                params = {
                    "keywords": keyword,
                    "location": JOB_LOCATION,
                    "start": page * 25,
                }
                resp = requests.get(SEARCH_URL, params=params, headers=HEADERS, timeout=10)
                resp.raise_for_status()

                soup = BeautifulSoup(resp.text, "lxml")

                for card in soup.select("li"):
                    title_tag = card.select_one(".base-search-card__title")
                    company_tag = card.select_one(".base-search-card__subtitle")
                    location_tag = card.select_one(".job-search-card__location")
                    link_tag = card.select_one("a.base-card__full-link")

                    if not title_tag or not link_tag:
                        continue

                    url = link_tag.get("href", "").split("?")[0]
                    job_id = url.rstrip("/").split("-")[-1] if url else None

                    if not job_id or job_id in seen_ids:
                        continue
                    seen_ids.add(job_id)

                    results.append({
                        "title": title_tag.get_text(strip=True),
                        "company": company_tag.get_text(strip=True) if company_tag else "N/A",
                        "location": location_tag.get_text(strip=True) if location_tag else JOB_LOCATION,
                        "url": url,
                        "source": "LinkedIn",
                        "category": category,
                        "id": f"linkedin_{job_id}",
                    })

    return results
