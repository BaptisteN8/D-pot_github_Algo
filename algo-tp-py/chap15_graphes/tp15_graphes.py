"""TP 15 — Les Graphes"""
from collections import deque


class Graph:
    def __init__(self, V: int):
        self.V   = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u: int, v: int) -> None:
        """Ajoute une arête non orientée. TODO"""
        raise NotImplementedError

    def add_directed_edge(self, u: int, v: int) -> None:
        """Ajoute une arête orientée u → v. TODO"""
        raise NotImplementedError

    def bfs(self, src: int) -> list:
        """BFS — retourne l'ordre de visite — O(V+E). TODO"""
        raise NotImplementedError

    def dfs(self, src: int) -> list:
        """DFS itératif avec pile — O(V+E). TODO"""
        raise NotImplementedError

    def _dfs_rec(self, u: int, visited: list, order: list) -> None:
        """Helper récursif pour dfs_recursive. TODO"""
        raise NotImplementedError

    def dfs_recursive(self, src: int) -> list:
        """DFS récursif — O(V+E). TODO"""
        raise NotImplementedError

    def is_connected(self) -> bool:
        """Graphe connexe ? — O(V+E). TODO"""
        raise NotImplementedError

    def _has_cycle_helper(self, u: int, parent: int, visited: list) -> bool:
        """DFS pour détecter un cycle dans un graphe non orienté. TODO"""
        raise NotImplementedError

    def has_cycle(self) -> bool:
        """Contient un cycle ? — O(V+E). TODO"""
        raise NotImplementedError

    def connected_components(self) -> int:
        """Nombre de composantes connexes — O(V+E). TODO"""
        raise NotImplementedError

    def _topo_helper(self, u: int, visited: list, stack: list) -> None:
        """DFS post-order pour le tri topologique. TODO"""
        raise NotImplementedError

    def topological_sort(self) -> list:
        """
        Tri topologique pour un DAG orienté — O(V+E).
        Retourne la liste des sommets dans l'ordre topologique.
        TODO
        """
        raise NotImplementedError
