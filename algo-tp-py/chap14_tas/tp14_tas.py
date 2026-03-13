"""TP 14 — Les Tas Binaires"""


class MinHeap:
    """Min-heap basé sur une liste Python."""

    def __init__(self):
        self._h = []

    def _sift_up(self, i: int) -> None:
        """Remontée — O(log n). TODO"""
        raise NotImplementedError

    def _sift_down(self, i: int) -> None:
        """Descente — O(log n). TODO"""
        raise NotImplementedError

    def insert(self, val) -> None:
        """Insère val — O(log n). TODO"""
        raise NotImplementedError

    def extract_min(self):
        """Extrait et retourne le minimum — O(log n). TODO"""
        raise NotImplementedError

    def get_min(self):
        """Retourne le minimum sans extraire — O(1). TODO"""
        raise NotImplementedError

    def build_heap(self, arr: list) -> None:
        """
        Construit le heap en O(n) depuis arr (algorithme de Floyd).
        TODO : copier arr dans self._h, puis for i in range(n//2-1, -1, -1): _sift_down(i)
        """
        raise NotImplementedError

    def __len__(self): return len(self._h)
    def is_empty(self): return len(self._h) == 0


def _sift_down_max(arr: list, n: int, i: int) -> None:
    """Max-heapify sur arr[0..n-1] depuis i. TODO"""
    raise NotImplementedError


def heap_sort(arr: list) -> None:
    """
    Tri par tas en place — O(n log n), O(1) espace.
    Phase 1 : buildMaxHeap en O(n)
    Phase 2 : extractions successives en O(n log n)
    TODO
    """
    raise NotImplementedError


def k_largest(arr: list, k: int) -> list:
    """
    Retourne les k plus grands éléments de arr (dans n'importe quel ordre).
    Complexité : O(n log k) avec un min-heap de taille k.
    TODO : si arr[i] > heap.get_min() → extract_min + insert
    """
    raise NotImplementedError


class TaskQueue:
    """File de priorité de tâches (priorité la plus basse = plus urgent)."""

    def __init__(self):
        self._heap = []

    def add_task(self, name: str, priority: int) -> None:
        """Ajoute une tâche — O(log n). TODO"""
        raise NotImplementedError

    def next_task(self) -> str:
        """Retourne et supprime la tâche la plus urgente — O(log n). TODO"""
        raise NotImplementedError

    def __len__(self): return len(self._heap)
