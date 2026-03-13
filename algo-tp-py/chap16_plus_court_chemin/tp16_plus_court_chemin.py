"""TP 16 — Algorithmes de Plus Court Chemin"""
import heapq
import math


def dijkstra(adj: list, src: int) -> tuple[list, list]:
    """
    Dijkstra avec min-heap (heapq).
    adj[u] = [(voisin, poids), ...]
    Retourne (dist[], prev[]) où prev[v] = prédécesseur de v sur le chemin optimal.
    Complexité : O((V+E) log V).
    TODO
    """
    raise NotImplementedError


def bellman_ford(edges: list, V: int, src: int) -> list | None:
    """
    Bellman-Ford pour graphes avec poids négatifs.
    edges = [(u, v, poids), ...]
    Retourne dist[] ou None si cycle négatif détecté.
    Complexité : O(V * E).
    TODO : V-1 relaxations ; V-ième → cycle négatif
    """
    raise NotImplementedError


def reconstruct_path(prev: list, src: int, dst: int) -> list:
    """
    Reconstruit le chemin de src à dst via prev[].
    Retourne [] si dst est inaccessible (prev[dst] == -1 et dst != src).
    TODO : remonter de dst à src par prev[], reverse
    """
    raise NotImplementedError
