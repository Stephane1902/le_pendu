# Jeu du pendu

Un jeu du pendu en Python avec une interface web, construit avec [Eel](https://github.com/python-eel/Eel) : la logique du jeu tourne en Python, l'interface (HTML / CSS / JavaScript) s'affiche dans le navigateur.

> Sur une idée originale de : https://www.jeudupendu.com/, implémenté par Stephane et Théo.

## Démarche de développement

Le projet a été réalisé en deux étapes, pour valider le concept avant d'investir dans l'interface :

1. **Prototype en console** (`console/pendu.py`) : une version minimale, jouable dans le terminal, écrite en un seul fichier. Elle sert à valider le concept et à fixer la logique du jeu : boucle de jeu, mot masqué par des `*`, lettres déjà essayées, compteur de vies, conditions de victoire et de défaite, et dessin du pendu en ASCII. Le mot à deviner y est écrit en dur et rien n'est sauvegardé.
2. **Version graphique avec Eel** : la logique validée en console est reprise et organisée en modules. Le choix du mot (`data/dict.txt`) et la gestion des coups (`src/game.py`) restent côté Python, l'affichage passe côté navigateur (`gui/`), et l'historique des parties est enregistré dans `data/games.csv`.

Les règles sont identiques dans les deux versions (une lettre à la fois, jamais deux fois la même, 6 erreurs maximum).

## Principe du jeu

Le jeu choisit au hasard un mot caché dans un dictionnaire. Le joueur doit retrouver ce mot lettre par lettre, en proposant des lettres une à une. Chaque lettre correcte se dévoile dans le mot, chaque lettre fausse fait apparaître une nouvelle partie du pendu.

## Règles

- Un mot est tiré au hasard dans `data/dict.txt`. Il est représenté par une suite de cases vides (`_`), une par lettre.
- À chaque tour, le joueur propose **une lettre** :
    - si la lettre est dans le mot, elle apparaît dans toutes les cases correspondantes (en vert) ;
    - sinon, le compteur d'erreurs augmente et une partie du pendu est dessinée (tête, corps, bras gauche, bras droit, jambe gauche, jambe droite).
- Une lettre ne peut être jouée qu'une seule fois : la touche est désactivée après avoir été utilisée (verte si elle était dans le mot, rouge sinon).
- **Victoire** : toutes les lettres du mot ont été trouvées avant la fin des essais.
- **Défaite** : le joueur atteint **6 erreurs**. Le mot complet est alors révélé.
- Chaque partie est enregistrée dans `data/games.csv` (date, mot, lettres jouées, nombre d'essais, nombre d'erreurs).

## Commandes

| Action                 | Commande                                                                                              |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
| Démarrer une partie    | Cliquer sur le bouton **Launch game** de la page d'accueil                                            |
| Proposer une lettre    | Cliquer sur une touche du clavier virtuel à l'écran (disposition AZERTY)                              |
| Recommencer une partie | Recharger la page de jeu (`F5`) : un nouveau mot est tiré                                             |
| Quitter                | Fermer l'onglet du navigateur : l'application Python s'arrête automatiquement après quelques secondes |

Dans la version console, on saisit une lettre au clavier puis on valide avec `Entrée` ; `Ctrl+C` quitte le jeu.

## Installation

### Prérequis

- Python 3.9 ou supérieur
- Un navigateur web (le jeu s'ouvre dans le navigateur par défaut)

### Étapes

1. Récupérer le projet :

    ```bash
    git clone <url-du-depot>
    cd <nom-du-dossier>
    ```

2. (Recommandé) Créer et activer un environnement virtuel :

    ```bash
    python -m venv .venv

    # Windows
    .venv\Scripts\activate

    # macOS / Linux
    source .venv/bin/activate
    ```

3. Installer les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Lancement

Depuis la racine du projet :

```bash
python main.py
```

Le jeu s'ouvre automatiquement dans le navigateur. Il faut lancer la commande depuis la racine du projet, car les chemins vers `gui/`, `src/` et `data/` sont relatifs.

### Version console

Le prototype console n'a besoin d'aucune dépendance (Python seul) :

```bash
python console/pendu.py
```

Le mot à deviner est défini en dur dans le fichier (variable `hidden_word`).

## Structure du projet

```
.
├── main.py            # Point d'entrée : initialise Eel et lance l'application
├── requirements.txt   # Dépendances Python
├── console/
│   └── pendu.py       # Prototype console (étape 1 de la démarche)
├── src/
│   └── game.py        # Logique du jeu (choix du mot, gestion des coups)
├── data/
│   ├── dict.txt       # Liste des mots possibles (un mot par ligne)
│   └── games.csv      # Historique des parties
└── gui/
    ├── main.html      # Page d'accueil
    ├── game.html      # Page de jeu
    ├── main.js
    ├── game.js        # Interactions de la page de jeu
    └── style.css
```

## Personnaliser le jeu

- **Ajouter des mots** : écrire un mot par ligne dans `data/dict.txt`. Le clavier ne contenant pas de lettres accentuées, mieux vaut utiliser des mots sans accents ni tirets.
- **Changer le nombre d'erreurs autorisées** : modifier `ERRORS_LIMIT` dans `src/game.py` (le dessin du pendu est prévu pour 6 erreurs).
