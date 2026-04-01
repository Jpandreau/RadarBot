import requests
from bs4 import BeautifulSoup
from config import JOB_KEYWORDS, JOB_LOCATION, JOB_RADIUS_KM
from scrapers.filters import is_it_related

BASE_URL = "https://www.hellowork.com"
SEARCH_URL = BASE_URL + "/fr-fr/emploi/recherche.html"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0"
}


def fetch_hellowork_jobs() -> list[dict]:
    results = []

    for category, keywords in JOB_KEYWORDS.items():
        for keyword in keywords:
            params = {"k": keyword, "l": JOB_LOCATION, "ray": JOB_RADIUS_KM}
            resp = requests.get(SEARCH_URL, params=params, headers=HEADERS, timeout=10)
            resp.raise_for_status()

            soup = BeautifulSoup(resp.text, "lxml")
            cards = soup.select("[data-cy=serpCard]")

            for card in cards:
                title_tag = card.select_one("[data-cy=offerTitle]")
                if not title_tag:
                    continue

                paragraphs = title_tag.select("p")
                title = paragraphs[0].get_text(strip=True) if len(paragraphs) > 0 else "N/A"
                if not is_it_related(title):
                    continue
                company = paragraphs[1].get_text(strip=True) if len(paragraphs) > 1 else "N/A"

                texts = list(card.stripped_strings)
                location = texts[2] if len(texts) > 2 else JOB_LOCATION

                href = title_tag.get("href", "")
                url = BASE_URL + href

                results.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "url": url,
                    "source": "Hellowork",
                    "category": category,
                    "id": href,
                })

    return results
