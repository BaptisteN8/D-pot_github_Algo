# TP 05 — La Récursion

## Exercice 1 — Classiques (6 pts)
- `power(x, n)` : x^n en **O(log n)** (exponentiation rapide)
- `gcd(a, b)` : PGCD par Euclide récursif
- `is_palindrome(s, l, r)` : palindrome récursif

## Exercice 2 — Tours de Hanoï (4 pts)
`hanoi(n, from_, to, via)` — retourne la liste des mouvements.
Complexité : O(2^n) mouvements (inévitable). Justifiez.

## Exercice 3 — Fibonacci avec mémoïsation (4 pts)
Comparez `fib_naive(n)` O(2^n) et `fib_memo(n)` O(n).
Comptez le nombre d'appels récursifs pour n=30.

## Exercice 4 — Permutations (3 pts)
`permutations(arr)` : toutes les permutations par backtracking.
Vérifiez qu'il y en a n! pour n éléments.

## Exercice 5 — Sous-ensembles (3 pts)
`subsets(arr)` : tous les sous-ensembles (2^n) par récursion.
