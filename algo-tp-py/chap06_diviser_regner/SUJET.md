# TP 06 — Diviser pour Régner

## Exercice 1 — Tri Fusion (7 pts)
`merge_sort(arr)` → nouveau tableau trié — **O(n log n)**, stable.
Sous-fonction `merge(left, right)`.

## Exercice 2 — Tri Rapide (7 pts)
`quick_sort(arr, lo, hi)` en place.
- `partition_fixed(arr, lo, hi)` : pivot = dernier élément
- `partition_random(arr, lo, hi)` : pivot aléatoire

## Exercice 3 — Quickselect (3 pts)
`quick_select(arr, lo, hi, k)` : k-ième plus petit (0-indexé) en **O(n)** moyen.

## Exercice 4 — Compter les inversions (3 pts)
Modifiez le tri fusion pour compter les paires (i,j) avec i<j et arr[i]>arr[j] — **O(n log n)**.
