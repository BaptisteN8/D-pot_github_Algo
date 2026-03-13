# TP 01 — Analyse de Complexité & Benchmarks

## Objectifs
- Mesurer empiriquement la complexité d'algorithmes
- Comprendre la différence entre O(1), O(n), O(log n), O(n²)
- Utiliser `time.perf_counter` pour chronométrer du code

## Exercice 1 — Analyser la complexité (6 pts)
Pour chaque fonction ci-dessous, **indiquez la complexité** dans le commentaire et **justifiez** :

```python
def func_a(n):        # Complexité ? TODO
    s = 0
    for i in range(n):
        for j in range(i, n):
            s += 1
    return s

def func_b(n):        # Complexité ? TODO
    c, i = 0, 1
    while i < n:
        c += 1
        i *= 2
    return c
```

## Exercice 2 — find_pair O(n²) vs O(n) (8 pts)
Implémentez deux versions qui cherchent deux éléments distincts dont la somme vaut `target` :
- `find_pair_naive(arr, target)` : deux boucles — **O(n²)**
- `find_pair_fast(arr, target)` : un passage + `set` — **O(n)**

## Exercice 3 — Benchmark (6 pts)
Complétez `run_benchmark()` qui mesure et compare les deux versions
pour n ∈ {1 000, 5 000, 10 000, 50 000}.
Expliquez pourquoi la version O(n) est ~n fois plus rapide.
