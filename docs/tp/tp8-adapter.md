# TP 8 : Adapter, recenser les oies et l'appeau électronique

**Partir de** `etape-0` · **Solution** `etape-1`

```
git switch -c tp8-binome-a origin/etape-0
```

Remplacez `binome-a` par le nom de votre binôme.

## Objectif

La réserve accueille une oie cendrée, Gertrude, et un appeau électronique qui imite le colvert. Tous deux viennent de la bibliothèque tierce `birdlib` (`src/birdlib/`), que Colvert ne peut pas modifier :
- l'oie (`Goose`) a une méthode `honk()` ;
- l'appeau (`ElectronicCall`) a une méthode `emit(frequency)`, qui demande une fréquence en hertz.

Le recensement ne connaît que `quack()`. Vous écrivez un **adaptateur** pour chacun : un objet qui offre `quack()` et traduit l'appel vers la méthode de `birdlib`.

**Les tests sont déjà écrits.** Au départ, `pytest` affiche `6 failed, 5 passed`.

## 1. Lire

- `src/colvert/ducks.py` : l'interface `Quackable` et un canard, `Mallard`.
- `src/birdlib/__init__.py` : `Goose` et `ElectronicCall`.
- `tests/test_adapters.py` : ce que les tests attendent.

## 2. L'adaptateur de l'oie

Dans `src/colvert/adapters.py`, complétez `GooseAdapter` :
- le constructeur reçoit une `Goose` et la garde dans un attribut ;
- `quack()` fait crier l'oie, et rend son cri.

Terminé quand : `pytest tests/test_adapters.py -k Goose` affiche `3 passed`.

## 3. L'adaptateur de l'appeau

Dans le même fichier, complétez `ElectronicCallAdapter` :
- le constructeur reçoit l'appeau **et la fréquence** à utiliser ;
- `quack()` rend ce que l'appeau émet à cette fréquence.

Terminé quand : `pytest tests/test_adapters.py` affiche `5 passed`.

## 4. Brancher

Dans `src/colvert/reserve.py`, ajoutez deux oiseaux à la réserve, à la fin du dictionnaire :
- `"Gertrude, oie cendrée"` : une oie de `birdlib`, adaptée ;
- `"Appeau électronique"` : un appeau de `birdlib`, adapté, réglé à 440 Hz.

Terminé quand : `pytest` affiche `11 passed`, et `python -m colvert` recense Gertrude et l'appeau.

## Règles

- Ne modifiez pas `src/birdlib/` ni les tests.
- Un adaptateur explicite : pas de `__getattr__`. Un test vérifie que l'adaptateur de l'oie n'offre pas `honk()`.

## Discuter

- `GooseAdapter` aurait pu hériter de `Goose`. Qu'y gagnerait-on, qu'y perdrait-on ?
- Qui décide de la fréquence de l'appeau : l'appeau, l'adaptateur, ou celui qui assemble la réserve ?
- Un adaptateur par `__getattr__` transmet tout appel inconnu à l'objet adapté. Pourquoi le test l'interdit-il ?
