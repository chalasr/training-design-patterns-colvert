# Étape 2 : solution du TP 9 (Decorator)

- `QuackCounter` est un **décorateur** au sens du GoF : il enveloppe un `Quackable`, ajoute un comportement (compter) et transmet l'appel à l'objet enveloppé.
- Il est lui-même un `Quackable` : `census()` le recense comme un canard, et un compteur peut envelopper un autre compteur.
- Chaque compteur a son propre compteur, `self.quacks`, créé dans `__init__`. Un attribut de classe (`QuackCounter.quacks += 1`) serait partagé par tous les compteurs.
- Les canards et les adaptateurs n'ont pas changé : le comptage est ajouté de l'extérieur, au moment de l'assemblage, dans `main()`.

## Adapter ou Decorator ?

Les deux enveloppent un objet. L'adaptateur **change l'interface** (`honk()` devient `quack()`) ; le décorateur **garde la même interface** et ajoute un comportement. On peut donc empiler des décorateurs, pas des adaptateurs.

## Le `@decorator` de Python

`demos/function_decorator.py` montre l'autre sens du mot :

```python
def count_calls(function: Callable[[], str]) -> Callable[[], str]:
    calls = 0

    @functools.wraps(function)
    def wrapper() -> str:
        nonlocal calls
        calls += 1
        print(f"  appel n° {calls} de {function.__name__}")
        return function()

    return wrapper
```

- `@count_calls` enveloppe une **fonction**, une fois pour toutes, au moment où elle est définie : tous ses appels sont comptés.
- `QuackCounter` enveloppe un **objet**, au moment où on le décide : on compte Gaston, et pas un autre colvert.
- `functools.wraps` recopie le nom et la documentation de la fonction d'origine sur `wrapper`.

## Dans votre quotidien

- La pile `io` : `open(path, "rb")` rend un `BufferedReader` qui enveloppe un `FileIO`. `gzip.GzipFile(fileobj=...)` enveloppe un fichier ouvert.
- Les middlewares WSGI : un middleware est une application WSGI qui en enveloppe une autre.
- Un repository avec cache, qui enveloppe le repository réel et garde les résultats.

## Le TP suivant

`src/colvert/flock.py` contient le squelette du TP 10, et `tests/test_flock.py` ses tests.
