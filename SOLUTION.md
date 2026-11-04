# Étape 0 : le code de départ

Pas de solution sur cette branche : c'est le point de départ du TP 8.

- Colvert recense trois canards : `python -m colvert`.
- La réserve accueille aussi une oie cendrée et un appeau électronique. Ils viennent de la bibliothèque tierce `birdlib`, qui ne connaît pas `quack()` : l'oie a `honk()`, l'appeau a `emit(frequency)`. Le recensement ne peut pas encore les compter.
- `src/colvert/adapters.py` contient les squelettes du TP 8, et `tests/test_adapters.py` ses tests.
- `demos/proxy.py` est la démonstration du Proxy, sans TP.
