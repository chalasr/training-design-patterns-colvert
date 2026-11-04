# Colvert : projet de travaux pratiques, formation Design Patterns

Colvert suit une réserve ornithologique : il recense les oiseaux de la réserve d'après leur cri. Ce dépôt est le code des travaux pratiques sur les patterns structuraux : Adapter, Decorator, Composite, et une démonstration de Proxy.

Tout le code tourne autour d'une seule interface, `Quackable` (`src/colvert/ducks.py`) : un objet qui sait pousser un cri, `quack() -> str`.

## Prérequis

- **Python 3.12 ou plus récent** et **Git**. Vérification : `python3 --version` et `git --version`.
- Un éditeur : PyCharm ou VS Code avec l'extension Python.

## Installation (une seule fois)

```
git clone https://github.com/chalasr/training-design-patterns-colvert colvert
cd colvert
python3 -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install -r requirements-dev.txt
pytest
```

Puis le recensement de la réserve :

```
python -m colvert
```

## Le code

| Fichier | Contenu |
|---|---|
| `src/colvert/ducks.py` | l'interface `Quackable` et les canards de la réserve |
| `src/colvert/census.py` | `census()`, le recensement : une ligne par oiseau, avec son cri |
| `src/colvert/reserve.py` | `build_reserve()`, les oiseaux de la réserve et leur nom |
| `src/colvert/__main__.py` | ce qu'affiche `python -m colvert` |
| `src/birdlib/` | une bibliothèque tierce : des oies et un appeau électronique. **On ne la modifie pas.** |
| `demos/` | les démonstrations du formateur |

## Vérifier son travail

```
pytest                     # les tests du projet
pytest -vv                 # une ligne par test, lue comme une phrase
python -m colvert          # le recensement
ruff check . && ruff format --check .
mypy
```

## Déroulé des TP

**Les tests de chaque TP sont déjà écrits.** Au départ, ils échouent : le code à écrire existe sous forme de squelettes qui lèvent `NotImplementedError`. Le TP est terminé quand `pytest` est entièrement vert.

Chaque étape corrigée a sa branche. **Chaque TP démarre de la branche de l'étape précédente**, dans une branche à vous (le préfixe `origin/` est nécessaire : après le clone, seule la branche par défaut, `etape-0`, existe en local) :

```
git switch -c tp8-binome-a origin/etape-0
```

| TP | Pattern | Partir de | Solution |
|---|---|---|---|
| [TP 8](docs/tp/tp8-adapter.md) | Adapter | `etape-0` | `etape-1` |
| [TP 9](docs/tp/tp9-decorator.md) | Decorator | `etape-1` | `etape-2` |
| [TP 10](docs/tp/tp10-composite.md) | Composite | `etape-2` | `etape-3` |

En retard ou bloqué ? Repartez de la solution : `git switch -c tp9-binome-a origin/etape-1`. Chaque branche contient un `SOLUTION.md` qui explique ses choix. Pour voir exactement ce qu'une étape a changé : `git diff origin/etape-0 origin/etape-1`.

Le test `tests/test_census_journey.py` passe **à toutes les étapes, sans modification** : c'est le filet de sécurité.

## L'IA pendant les TP

Écrivez le code vous-mêmes : c'est en écrivant un pattern qu'on l'apprend. L'assistant sert de **relecteur** une fois votre version écrite (voir [AGENTS.md](AGENTS.md)).
