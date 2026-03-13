"""TP 09 — Les Files (FIFO)"""
from collections import deque


class CircularQueue:
    """File circulaire à capacité fixe."""

    def __init__(self, capacity: int = 64):
        self._cap = capacity
        self._data = [None] * capacity
        self._front = 0
        self._rear  = 0
        self._size  = 0

    def enqueue(self, val) -> None:
        """Enfile val — O(1). Lève OverflowError si plein. TODO"""
        raise NotImplementedError

    def dequeue(self):
        """Défile et retourne la valeur — O(1). Lève IndexError si vide. TODO"""
        raise NotImplementedError

    def front(self):
        """Retourne la valeur en tête sans défiler — O(1). TODO"""
        raise NotImplementedError

    def is_empty(self) -> bool: return self._size == 0
    def is_full(self)  -> bool: return self._size == self._cap
    def __len__(self)  -> int:  return self._size


class MinPriorityQueue:
    """File de priorité min-heap — priorité la plus basse sort en premier."""

    def __init__(self):
        self._heap = []   # éléments : (priority, val)

    def _sift_up(self, i: int) -> None:
        """Remontée après insertion. TODO"""
        raise NotImplementedError

    def _sift_down(self, i: int) -> None:
        """Descente après extraction. TODO"""
        raise NotImplementedError

    def insert(self, val, priority: int) -> None:
        """Insère val avec priority — O(log n). TODO"""
        raise NotImplementedError

    def extract_min(self):
        """Extrait la valeur de plus basse priorité — O(log n). TODO"""
        raise NotImplementedError

    def peek_min(self):
        """Retourne la valeur min sans extraire — O(1). TODO"""
        raise NotImplementedError

    def __len__(self): return len(self._heap)


def bfs(adj: list, src: int) -> list:
    """BFS — retourne l'ordre de visite des sommets — O(V+E). TODO"""
    raise NotImplementedError


def shortest_path(adj: list, src: int, dst: int) -> int:
    """
    Retourne le nombre minimum d'arêtes entre src et dst.
    Retourne -1 si dst est inaccessible depuis src.
    TODO
    """
    raise NotImplementedError


class TreeNode:
    def __init__(self, val):
        self.val   = val
        self.left  = None
        self.right = None


def level_order(root: TreeNode | None) -> list:
    """
    Parcours en largeur d'un arbre binaire.
    Retourne list[list[int]] — une liste par niveau.
    TODO
    """
    raise NotImplementedError
