# TP 9 : Decorator, compter les cris sans modifier les canards

**Partir de** `etape-1` · **Solution** `etape-2`

```
git switch -c tp9-binome-a origin/etape-1
```

## Objectif

Pour le recensement, Colvert veut savoir combien de cris il a entendus. Les canards ne doivent pas changer : ni `Mallard`, ni `Teal`, ni `RubberDuck`, ni les adaptateurs du TP 8.

Vous écrivez un **décorateur** au sens du GoF : un objet qui enveloppe un `Quackable`, compte chaque cri, et laisse passer le cri sans le modifier. Il est lui-même un `Quackable` : on peut le recenser, et même l'envelopper à son tour.

**Les tests sont déjà écrits.** Au départ, `pytest` affiche `8 failed, 10 passed`.

## 1. Lire

- `tests/test_counting.py` : ce que les tests attendent de `QuackCounter`.
- `src/colvert/adapters.py` : votre TP 8 enveloppait déjà un objet. Qu'est-ce qui change ici ?

## 2. Le compteur

Dans `src/colvert/counting.py`, complétez `QuackCounter` :
- le constructeur reçoit l'oiseau à envelopper, le garde, et met son compteur `quacks` à zéro ;
- `quack()` ajoute 1 au compteur, puis rend le cri de l'oiseau enveloppé.

Terminé quand : `pytest tests/test_counting.py` affiche `7 passed`.

## 3. Brancher

Dans `src/colvert/__main__.py`, la fonction `main()` :
- enveloppe chaque oiseau de la réserve dans un `QuackCounter`, en gardant son nom ;
- recense ces oiseaux comptés ;
- affiche en dernière ligne le total des cris comptés : `Cris comptés : 5`.

Terminé quand : `pytest` affiche `18 passed`, et `python -m colvert` finit par `Cris comptés : 5`.

## Règles

- Ne modifiez ni les canards, ni les adaptateurs, ni les tests.
- Chaque compteur compte les cris de **son** oiseau.

## Discuter

- Le compteur enveloppe un objet, comme l'adaptateur du TP 8. Quelle est la différence entre les deux ?
- `QuackCounter(QuackCounter(Mallard()))` : que comptent les deux compteurs ?
- Python a aussi des décorateurs, avec `@`. Qu'enveloppent-ils, et à quel moment ?
