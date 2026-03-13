# TP 17 — Recherche Informée : A*

## Exercice 1 — Heuristiques (4 pts)
- `manhattan(a, b)` = |Δr| + |Δc|
- `chebyshev(a, b)` = max(|Δr|, |Δc|)
- `euclidean(a, b)` = sqrt(Δr² + Δc²)

## Exercice 2 — A* sur grille 2D (12 pts)
`astar(grid, start, end, h)` :
- `grid` : `list[str]`, `'.'` = libre, `'#'` = mur
- Retourne la liste de positions `(r, c)` du chemin, ou `[]`
- Mouvements 4-directionnels
- `h` : heuristique à utiliser (paramètre callable)

## Exercice 3 — Comparaison A* vs BFS (4 pts)
`astar_with_count` et `bfs_with_count` : mesurent les cellules explorées.
Sur un labyrinthe, A* doit en explorer moins que BFS.
