# TP 03 — Les Tris Simples

## Exercice 1 — Implémenter les trois tris (9 pts)
- `bubble_sort(arr)` : avec flag `swapped` pour le cas O(n) meilleur
- `selection_sort(arr)` : toujours O(n²), minimum n-1 échanges
- `insertion_sort(arr)` : O(n) sur tableau trié, O(n²) pire

## Exercice 2 — Tri générique (4 pts)
Paramètre `key` et `reverse` comme `sorted()` :
```python
insertion_sort_generic(arr, key=lambda x: x, reverse=False)
```

## Exercice 3 — Stabilité (3 pts)
Parmi les trois tris, lesquels sont stables ?
Démontrez avec des `(valeur, indice_original)`.

## Exercice 4 — Benchmark (4 pts)
Mesurez pour n = 500, 2000, 5000 sur tableau aléatoire, trié, et inversé.
Quel tri bénéficie le plus du meilleur cas ? Pourquoi ?
