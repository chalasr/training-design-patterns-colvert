# Étape 3 : solution du TP 10 (Composite)

- `Flock` est un **composite** : un `Quackable` qui contient des `Quackable`. Ses membres sont des **feuilles** (un canard, une oie adaptée, un compteur) ou d'autres composites (une volée).
- `Flock.quack()` demande son cri à chaque membre, sans savoir ce qu'il est. Quand un membre est une volée, son propre `quack()` interroge ses membres à son tour : c'est une **récursion**, que personne n'a écrite explicitement. Elle s'arrête aux feuilles.
- `census()` n'a pas changé : il recense une volée comme un seul oiseau.
- `__iter__()` rend un itérateur sur la liste des membres : `for bird in flock:` et `list(flock)` fonctionnent.
- `Flock(*birds)` reçoit les membres en nombre quelconque : `Flock(Mallard(), Teal())`.

## Les quatre patterns ensemble

La « volée de passage » contient deux oies adaptées (Adapter) et une petite volée (Composite). Dans `main()`, chaque entrée de la réserve est enveloppée dans un `QuackCounter` (Decorator). Aucun `isinstance` nulle part.

`python -m colvert` affiche `Cris comptés : 7` : chaque compteur compte les appels à `quack()` de **son** objet, et une volée répond en une fois. Pour compter chaque oiseau, il faut envelopper chaque oiseau avant de le mettre dans la volée.

## Les opérations qui n'ont pas de sens sur une feuille

`add()` existe sur `Flock`, pas sur `Mallard`. Le GoF discute de mettre `add()` dans l'interface commune, pour que feuilles et composites soient interchangeables en tout point : il faut alors décider ce que fait `add()` sur un canard (lever une exception ?). Ici, l'interface commune se limite à `quack()`, et seul celui qui construit une volée appelle `add()`.

## Dans votre quotidien

- Le module `ast` : un nœud `Module` contient des instructions, qui contiennent des expressions, qui contiennent des expressions.
- La collecte de pytest : une session contient des modules, qui contiennent des classes, qui contiennent des tests.
- Les composants d'une interface graphique, ou d'une page React : un composant contient des composants.
