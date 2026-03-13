# TP 02 — Les Tableaux

## Exercice 1 — Opérations classiques (6 pts)
- `rotate(arr, k)` : rotation circulaire droite de k positions — **O(n)**
  *(Astuce : reverse tout, reverse [0,k-1], reverse [k,n-1])*
- `remove_duplicates(arr)` : supprime les doublons d'un tableau **trié** — **O(n)**
- `merge_arrays(a, b)` : fusionne deux tableaux **triés** — **O(n+m)**

## Exercice 2 — Recherche binaire (6 pts)
- `binary_search(arr, target)` → indice ou -1 — **O(log n)**
- `lower_bound(arr, target)` → premier i tel que arr[i] >= target — **O(log n)**
- `upper_bound(arr, target)` → premier i tel que arr[i] > target — **O(log n)**

## Exercice 3 — Matrices (4 pts)
- `transpose(m)` : transposée d'une matrice n×n **en place** — **O(n²)**
- `rotate_90(m)` : rotation 90° sens horaire — **O(n²)**

## Exercice 4 — Algorithme de Kadane (4 pts)
Sous-tableau contigu de somme maximale en **O(n)**.
Exemple : `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` → 6
