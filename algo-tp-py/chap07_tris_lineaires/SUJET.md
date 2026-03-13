# TP 07 — Les Tris Linéaires

## Exercice 1 — Counting Sort (7 pts)
`counting_sort(arr, k)` pour des entiers dans [0, k] — **O(n+k)**, stable.

## Exercice 2 — Radix Sort LSD (7 pts)
`radix_sort(arr)` chiffre par chiffre du moins au plus significatif — **O(d(n+10))**.
Sous-routine : `count_sort_by_digit(arr, exp)`.

## Exercice 3 — Bucket Sort (3 pts)
`bucket_sort(arr)` pour des flottants dans [0.0, 1.0) — **O(n)** moyen.

## Exercice 4 — Comparaison (3 pts)
Benchmarkez counting sort vs `sorted()` pour n=100 000 entiers dans [0, 999].
