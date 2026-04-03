from dotenv import load_dotenv
import os

load_dotenv()


def _env_list(key: str, default: list[str]) -> list[str]:
    value = os.getenv(key, "")
    if not value.strip():
        return default
    return [item.strip() for item in value.split(",") if item.strip()]


def _env_int(key: str, default: int) -> int:
    raw = os.getenv(key)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _env_float(key: str, default: float) -> float:
    raw = os.getenv(key)
    if raw is None:
        return default
    try:
        return float(raw)
    except ValueError:
        return default


# URL du webhook Discord (obligatoire).
# Compatible avec DISCORD_WEBHOOK_URL, WEBHOOK et webhook.
DISCORD_WEBHOOK_URL = (
    os.getenv("DISCORD_WEBHOOK_URL")
    or os.getenv("WEBHOOK")
    or os.getenv("webhook")
)

# Mots-clés par catégorie.
# La catégorie détermine la couleur de la notification Discord.
# Modifier ici pour personnaliser les recherches.
JOB_KEYWORDS = {
    "Développement": ["stage développeur", "stage informatique"],
    "Cybersécurité": ["stage cybersécurité"],
    "Réseau": ["stage réseau"],
    "Data": ["stage data"],
}

# Zone de recherche.
JOB_LOCATION = os.getenv("JOB_LOCATION", "Moulins, Allier")
JOB_LAT = _env_float("JOB_LAT", 46.5647)
JOB_LNG = _env_float("JOB_LNG", 3.3322)
JOB_RADIUS_KM = _env_int("JOB_RADIUS_KM", 150)

# Sources actives. Valeurs supportées : wtj, hellowork, linkedin.
JOB_SOURCES = [s.lower() for s in _env_list("JOB_SOURCES", ["linkedin", "hellowork", "wtj"])]

# Nombre de pages LinkedIn scannées par mot-clé (25 offres/page).
LINKEDIN_MAX_PAGES = max(1, _env_int("LINKEDIN_MAX_PAGES", 2))

# Filtre contrat : l'offre doit contenir au moins un de ces termes.
ALTERNANCE_REQUIRED_TERMS = _env_list(
    "ALTERNANCE_REQUIRED_TERMS",
    ["stage"],
)

# Filtre contrat : l'offre est rejetée si elle contient un de ces termes.
EXCLUDED_JOB_TERMS = _env_list(
    "EXCLUDED_JOB_TERMS",
    ["alternance", "apprentissage", "cdi", "cdd", "freelance", "interim", "intérim"],
)

# Fréquence de scan en heures.
CHECK_INTERVAL_HOURS = max(1, _env_int("CHECK_INTERVAL_HOURS", 6))


def validate_config() -> None:
    if not DISCORD_WEBHOOK_URL:
        raise ValueError("Webhook manquant : définir DISCORD_WEBHOOK_URL dans .env")
    if not JOB_KEYWORDS:
        raise ValueError("JOB_KEYWORDS ne peut pas être vide")
    if not JOB_SOURCES:
        raise ValueError("JOB_SOURCES ne peut pas être vide")
