"""TP 08 — Les Piles (LIFO)"""


class Stack:
    """Pile générique basée sur une liste Python."""

    def __init__(self):
        self._data = []

    def push(self, val) -> None:
        """Empile val — O(1). TODO"""
        raise NotImplementedError

    def pop(self):
        """Dépile et retourne le sommet — O(1). Lève IndexError si vide. TODO"""
        raise NotImplementedError

    def peek(self):
        """Retourne le sommet sans dépiler — O(1). Lève IndexError si vide. TODO"""
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self._data)


def is_balanced(expr: str) -> bool:
    """
    Vérifie que les parenthèses/accolades/crochets sont équilibrés — O(n).
    TODO
    """
    raise NotImplementedError


def eval_rpn(tokens: list[str]) -> int:
    """
    Évalue une expression en notation polonaise inverse (RPN).
    Opérateurs supportés : +, -, *, /  (division entière tronquée vers 0).
    TODO
    """
    raise NotImplementedError


class MinStack:
    """Pile avec get_min() en O(1) — deux piles internes."""

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        """TODO"""
        raise NotImplementedError

    def pop(self) -> int:
        """TODO"""
        raise NotImplementedError

    def top(self) -> int:
        """TODO"""
        raise NotImplementedError

    def get_min(self) -> int:
        """Retourne le minimum actuel en O(1). TODO"""
        raise NotImplementedError


def sort_stack(s: Stack) -> None:
    """
    Trie la pile s (croissant en haut) avec UNE SEULE pile auxiliaire.
    Algorithme d'insertion — O(n²).
    TODO
    """
    raise NotImplementedError
