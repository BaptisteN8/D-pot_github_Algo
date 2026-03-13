"""
TP 03 — Les Tris Simples
Toutes les fonctions trient en place (modifient arr).
"""


def bubble_sort(arr: list) -> None:
    """
    Tri à bulles avec optimisation flag swapped.
    Complexité : O(n²) pire, O(n) meilleur (tableau déjà trié).
    TODO
    """
    raise NotImplementedError


def selection_sort(arr: list) -> None:
    """
    Tri par sélection du minimum.
    Complexité : toujours O(n²), au plus n-1 échanges.
    TODO
    """
    raise NotImplementedError


def insertion_sort(arr: list) -> None:
    """
    Tri par insertion.
    Complexité : O(n²) pire, O(n) meilleur.
    TODO : pour i=1..n-1 : key=arr[i], décaler droite tant que arr[j]>key
    """
    raise NotImplementedError


def insertion_sort_generic(arr: list, key=None, reverse: bool = False) -> None:
    """
    Tri par insertion avec comparateur.
    key   : fonction d'extraction de clé (défaut : identité)
    reverse : si True, tri décroissant
    Complexité : O(n²)
    TODO
    """
    raise NotImplementedError
