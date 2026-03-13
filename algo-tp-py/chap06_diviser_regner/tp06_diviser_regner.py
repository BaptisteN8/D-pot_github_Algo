"""
TP 06 — Diviser pour Régner
"""
import random


def merge(left: list, right: list) -> list:
    """
    Fusionne deux listes triées en une seule triée.
    Stable : les éléments égaux de left précèdent ceux de right.
    Complexité : O(n+m). TODO
    """
    raise NotImplementedError


def merge_sort(arr: list) -> list:
    """
    Tri fusion — retourne un nouveau tableau trié.
    Complexité : O(n log n) temps, O(n) espace. TODO
    """
    raise NotImplementedError


def partition_fixed(arr: list, lo: int, hi: int) -> int:
    """
    Partition avec arr[hi] comme pivot.
    Retourne la position finale du pivot. TODO
    """
    raise NotImplementedError


def partition_random(arr: list, lo: int, hi: int) -> int:
    """
    Choisit un pivot aléatoire dans [lo, hi], l'échange avec arr[hi],
    puis appelle partition_fixed. TODO
    """
    raise NotImplementedError


def quick_sort(arr: list, lo: int = 0, hi: int = None) -> None:
    """
    Tri rapide en place avec pivot aléatoire.
    Complexité : O(n log n) espérance, O(n²) pire cas. TODO
    """
    raise NotImplementedError


def quick_select(arr: list, lo: int, hi: int, k: int) -> int:
    """
    k-ième plus petit élément (0-indexé) dans arr[lo..hi].
    Complexité : O(n) espérance. TODO
    """
    raise NotImplementedError


def count_inversions(arr: list) -> tuple[list, int]:
    """
    Retourne (arr_trié, nb_inversions).
    Une inversion = paire (i,j) avec i<j et arr[i]>arr[j].
    Complexité : O(n log n). TODO : modifier merge pour compter
    """
    raise NotImplementedError
