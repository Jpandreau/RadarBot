# RadarBot

Bot Python qui détecte des offres d'alternance IT (LinkedIn, Hellowork, Welcome to the Jungle) et envoie des notifications Discord avec couleur par catégorie.

---

## Fonctionnalités

- Sources : **LinkedIn**, **Hellowork**, **Welcome to the Jungle**
- Mots-clés organisés par **catégorie** (Développement, Cybersécurité, Réseau, Data)
- Filtre strict **alternance** — rejette les stages, CDI, CDD automatiquement
- Notifications **Discord** avec couleur par catégorie et titre cliquable
- Déduplication — aucune offre envoyée deux fois
- Scan automatique toutes les **6 heures**

---

## Structure du projet

```
RadarBot/
├── scrapers/
│   ├── wtj.py          # Welcome to the Jungle (Algolia API)
│   ├── hellowork.py    # Hellowork (HTML)
│   └── linkedin.py     # LinkedIn (guest API)
├── main.py             # Point d'entrée + filtre contrat + boucle
├── config.py           # Configuration (mots-clés, filtres, sources)
├── notifier.py         # Notifications Discord
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── .gitignore
```

---

## Démarrage rapide

### Docker (recommandé)

```bash
git clone git@github.com:Jpandreau/RadarBot.git
cd RadarBot
cp .env.example .env
# Remplir DISCORD_WEBHOOK_URL dans .env
docker compose up -d --build
```

Logs :
```bash
docker compose logs -f
```

Arrêt :
```bash
docker compose down
```

### Python (3.12+)

```bash
git clone git@github.com:Jpandreau/RadarBot.git
cd RadarBot
pip3 install -r requirements.txt
cp .env.example .env
# Remplir DISCORD_WEBHOOK_URL dans .env
python3 main.py
```

---

## Configuration

### Mots-clés et catégories — `config.py`

Les mots-clés sont organisés par catégorie dans `config.py`. Chaque catégorie a sa couleur dans Discord.

```python
JOB_KEYWORDS = {
    "Développement": ["Alternance Développeur web", "Alternance Développeur Full Stack"],
    "Cybersécurité": ["Alternance Cybersécurité"],
    "Réseau":        ["Alternance Réseau"],
    "Data":          ["Alternance Data"],
}
```

Pour ajouter une catégorie ou un mot-clé, modifier directement `config.py`.

### Variables d'environnement — `.env`

Les paramètres avancés peuvent être surchargés via `.env` (copier `.env.example`) :

| Variable | Description | Défaut |
|---|---|---|
| `DISCORD_WEBHOOK_URL` | Webhook Discord **(obligatoire)** | — |
| `JOB_SOURCES` | Sources actives (linkedin,hellowork,wtj) | toutes |
| `JOB_LOCATION` | Ville/zone de recherche | Moulins, Allier |
| `JOB_RADIUS_KM` | Rayon de recherche en km | 150 |
| `ALTERNANCE_REQUIRED_TERMS` | Termes requis dans le titre | alternance,apprentissage |
| `EXCLUDED_JOB_TERMS` | Termes interdits dans le titre | stage,cdi,cdd,... |
| `LINKEDIN_MAX_PAGES` | Pages LinkedIn par mot-clé | 2 |
| `CHECK_INTERVAL_HOURS` | Intervalle de scan en heures | 6 |

---

## Dépannage

| Problème | Solution |
|---|---|
| Erreur webhook | Vérifier `DISCORD_WEBHOOK_URL` dans `.env` |
| Aucune offre | Augmenter `JOB_RADIUS_KM`, assouplir les mots-clés |
| Trop d'offres hors cible | Ajouter des termes dans `EXCLUDED_JOB_TERMS` |
| Offres alternance manquées | Réduire `ALTERNANCE_REQUIRED_TERMS` |

---

## Dépendances

- `requests`
- `beautifulsoup4`
- `lxml`
- `python-dotenv`
- `schedule`

---

## Convention de commits

| Tag | Usage |
|---|---|
| `[ADD]` | Nouveau fichier ou fonctionnalité |
| `[FIX]` | Correction de bug |
| `[REM]` | Suppression |
| `[CODINGSTYLE]` | Formatage, nommage, style |
| `[REFACTOR]` | Restructuration sans changement de comportement |
| `[DOCS]` | README, commentaires, documentation |
