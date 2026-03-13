# TP 16 — Algorithmes de Plus Court Chemin

## Exercice 1 — Dijkstra (10 pts)
`dijkstra(adj, src)` avec `heapq` — O((V+E) log V).
Retourner `(dist, prev)` pour reconstruire les chemins.

## Exercice 2 — Bellman-Ford (6 pts)
`bellman_ford(edges, V, src)` — O(V·E).
Retourner `None` si cycle négatif détecté.

## Exercice 3 — Reconstruction du chemin (4 pts)
`reconstruct_path(prev, src, dst)` → liste de sommets.
