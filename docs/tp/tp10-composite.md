# TP 10 : Composite, recenser une volée comme un seul oiseau

**Partir de** `etape-2` · **Solution** `etape-3`

```
git switch -c tp10-binome-a origin/etape-2
```

## Objectif

Des volées se posent sur la réserve. Le recensement doit pouvoir recenser une volée **comme un seul oiseau** : elle répond à `quack()` par les cris de tous ses membres.

Une volée (`Flock`) est donc un `Quackable` qui contient des `Quackable` : des canards, des oies adaptées, des oiseaux comptés, et même d'autres volées. Ni la volée ni le recensement ne demandent ce qu'est chaque membre : aucun `isinstance`.

**Les tests sont déjà écrits.** Au départ, `pytest` affiche `7 failed, 18 passed`.

## 1. Lire

- `tests/test_flock.py` : ce que les tests attendent de `Flock`.

## 2. La volée

Dans `src/colvert/flock.py`, complétez `Flock` :
- le constructeur reçoit les membres de la volée, en nombre quelconque : `Flock(Mallard(), Teal())`. Il les garde dans une liste ;
- `add(bird)` ajoute un membre ;
- `quack()` rend les cris de tous les membres, dans l'ordre, séparés par une virgule et une espace : `"Coin-coin, Krik-krik"`. Une volée vide rend `""` ;
- `__iter__()` permet de parcourir les membres : `for bird in flock:`.

Terminé quand : `pytest tests/test_flock.py` affiche `7 passed`.

## 3. Brancher

Dans `src/colvert/reserve.py`, ajoutez deux volées à la fin de la réserve :
- `"Volée de l'étang nord"` : deux colverts et une sarcelle ;
- `"Volée de passage"` : deux oies adaptées, et une petite volée d'un colvert et d'une sarcelle.

Terminé quand : `pytest` affiche `25 passed`, et `python -m colvert` recense les deux volées.

## Règles

- Ne modifiez pas `census()`, ni les tests.
- Pas de `isinstance` dans `flock.py` : un test le vérifie.

## Discuter

- `census()` n'a pas changé. Comment recense-t-il une volée de volées ?
- `python -m colvert` affiche `Cris comptés : 7`, alors que la réserve pousse plus de cris. Pourquoi ? Où placer les compteurs pour compter chaque oiseau ?
- Faut-il une méthode `add()` sur `Mallard`, pour que canards et volées aient exactement la même interface ?
