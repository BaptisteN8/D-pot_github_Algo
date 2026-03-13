"""TP 17 — Recherche Informée : A*"""
import heapq
import math


# ── Exercice 1 ──────────────────────────────────────────────────────────────

def manhattan(a: tuple, b: tuple) -> int:
    """Distance de Manhattan — |Δr| + |Δc|. TODO"""
    raise NotImplementedError


def chebyshev(a: tuple, b: tuple) -> int:
    """Distance de Chebyshev — max(|Δr|, |Δc|). TODO"""
    raise NotImplementedError


def euclidean(a: tuple, b: tuple) -> float:
    """Distance euclidienne — sqrt(Δr²+Δc²). TODO"""
    raise NotImplementedError


# ── Exercice 2 ──────────────────────────────────────────────────────────────

def astar(grid: list, start: tuple, end: tuple,
          h=None) -> list:
    """
    A* sur grille 2D — retourne le chemin ou [] si impossible.
    grid[r][c] == '#' = mur.
    Mouvements : 4-directionnels (haut, bas, gauche, droite).
    h : heuristique admissible (défaut : manhattan)

    TODO :
    g[pos] = coût réel depuis start
    open = min-heap sur f = g + h(pos, end)
    Pour chaque voisin accessible : relaxer si ng < g[voisin]
    """
    if h is None:
        h = manhattan
    raise NotImplementedError


# ── Exercice 3 ──────────────────────────────────────────────────────────────

def astar_with_count(grid, start, end, h=None):
    """
    Identique à astar() mais retourne aussi le nombre de cellules explorées.
    Retourne (path, explored_count).
    TODO
    """
    raise NotImplementedError


def bfs_on_grid(grid: list, start: tuple, end: tuple) -> list:
    """
    BFS sur la même grille — retourne le chemin optimal.
    TODO
    """
    raise NotImplementedError


def bfs_with_count(grid, start, end):
    """
    BFS avec compteur de cellules explorées.
    Retourne (path, explored_count).
    TODO
    """
    raise NotImplementedError
