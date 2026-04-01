import re

# Regex pour vérifier qu'une offre est liée à l'informatique.
# Appliqué sur le titre de l'offre.
IT_PATTERN = re.compile(
    r"\b("
    r"informatique|développeur|developpeur|software|engineer|ingénieur logiciel|"
    r"python|java|javascript|react|angular|vue|web|backend|frontend|"
    r"fullstack|full.stack|réseau|cybersécurité|machine learning|"
    r"cloud|devops|data|système d.information|systèmes informatiques|"
    r"numérique|programmation|algorithme|sécurité informatique"
    r")\b",
    re.IGNORECASE,
)


def is_it_related(title: str) -> bool:
    return bool(IT_PATTERN.search(title))
