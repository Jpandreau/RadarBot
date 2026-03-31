import re
import requests
from config import JOB_KEYWORDS, JOB_LOCATION, JOB_LAT, JOB_LNG, JOB_RADIUS_KM

ALGOLIA_URL = "https://csekhvms53-1.algolianet.com/1/indexes/*/queries"
ALGOLIA_HEADERS = {
    "x-algolia-application-id": "CSEKHVMS53",
    "x-algolia-api-key": "4bd8f6215d0cc52b26430765769e65a0",
    "Content-Type": "application/json",
    "Origin": "https://www.welcometothejungle.com",
    "Referer": "https://www.welcometothejungle.com/",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0",
}


IT_PATTERN = re.compile(
    r"\b("
    r"informatique|développeur|developpeur|software|engineer|ingénieur logiciel|"
    r"python|java|javascript|react|angular|vue|web|backend|frontend|"
    r"fullstack|full.stack|réseau|cybersécurité|machine learning|"
    r"cloud|devops|data|devops|système d.information|systèmes informatiques|"
    r"numérique|programmation|algorithme|sécurité informatique"
    r")\b",
    re.IGNORECASE,
)


def is_it_related(title: str) -> bool:
    return bool(IT_PATTERN.search(title))


def fetch_wtj_jobs() -> list[dict]:
    results = []

    for keyword in JOB_KEYWORDS:
        payload = {
            "requests": [{
                "indexName": "wttj_jobs_production_fr",
                "params": f"query={keyword}&hitsPerPage=50&aroundLatLng={JOB_LAT},{JOB_LNG}&aroundRadius={JOB_RADIUS_KM * 1000}",
            }]
        }

        resp = requests.post(ALGOLIA_URL, json=payload, headers=ALGOLIA_HEADERS, timeout=10)
        resp.raise_for_status()
        hits = resp.json()["results"][0]["hits"]

        for hit in hits:
            title = hit.get("name", "N/A")
            if not is_it_related(title):
                continue
            results.append({
                "title": title,
                "company": hit.get("organization", {}).get("name", "N/A"),
                "location": hit.get("offices", [{}])[0].get("city", JOB_LOCATION),
                "url": f"https://www.welcometothejungle.com/fr/companies/{hit.get('organization', {}).get('slug', '')}/jobs/{hit.get('slug', '')}",
                "source": "WTJ",
                "id": hit.get("objectID"),
            })

    return results
