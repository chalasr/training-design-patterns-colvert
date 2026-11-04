# Étape 1 : solution du TP 8 (Adapter)

- `GooseAdapter` et `ElectronicCallAdapter` sont des **adaptateurs** : ils offrent l'interface que Colvert attend, `quack()`, et traduisent l'appel vers celle de `birdlib`, `honk()` ou `emit(frequency)`.
- Chaque adaptateur reçoit l'objet adapté dans son constructeur et le garde : c'est de la **composition**. `birdlib` n'a pas changé, ni `census()`.
- `ElectronicCallAdapter` reçoit aussi la fréquence : `quack()` n'a pas de paramètre, `emit()` en demande un. C'est l'adaptateur qui comble la différence, et c'est `build_reserve()` qui choisit la valeur, 440 Hz.
- `build_reserve()` assemble la réserve : c'est le seul endroit qui sait que Gertrude vient de `birdlib`.

## Pourquoi pas l'héritage ?

`class GooseAdapter(Goose)` marcherait aussi : c'est l'« adaptateur de classe » du GoF. Mais l'adaptateur hériterait alors de `honk()`, et de tout ce que `birdlib` ajoutera à `Goose`. Il ne pourrait pas non plus adapter une oie déjà créée par `birdlib`.

## Pourquoi pas `__getattr__` ?

```python
class GooseAdapter:
    def __init__(self, goose: Goose) -> None:
        self.goose = goose

    def quack(self) -> str:
        return self.goose.honk()

    def __getattr__(self, name: str) -> Any:
        return getattr(self.goose, name)
```

`__getattr__` est appelé quand un attribut n'existe pas sur l'objet : ici, il transmet tout appel inconnu à l'oie. C'est court, mais l'adaptateur offre alors toute l'interface de `Goose`, sans qu'on le voie en lisant la classe, et `mypy` ne peut plus rien vérifier. Le test `test_the_adapter_only_offers_the_duck_interface` l'interdit.

## Dans votre quotidien

- `io.TextIOWrapper` adapte un flux binaire en flux texte : `open(path)` vous le rend sans que vous le voyiez.
- Un SDK de paiement ou d'envoi de SMS, placé derrière une interface de votre application : le jour où vous changez de fournisseur, seul l'adaptateur change.

## Le TP suivant

`src/colvert/counting.py` contient le squelette du TP 9, et `tests/test_counting.py` ses tests.
