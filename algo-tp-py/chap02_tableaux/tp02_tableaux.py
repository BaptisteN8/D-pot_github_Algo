"""
TP 02 — Les Tableaux
Complétez les fonctions marquées TODO
"""


def rotate(arr: list, k: int) -> None:
    """
    Rotation circulaire droite de k positions, en place.
    Complexité attendue : O(n) temps, O(1) espace.
    Astuce : triple reverse.
    TODO
    """
    raise NotImplementedError


def remove_duplicates(arr: list) -> int:
    """
    Supprime les doublons d'un tableau TRIÉ en place.
    Retourne la nouvelle longueur.
    Complexité attendue : O(n).
    TODO
    """
    raise NotImplementedError


def merge_arrays(a: list, b: list) -> list:
    """
    Fusionne deux tableaux triés en un seul tableau trié.
    Complexité attendue : O(n+m).
    TODO
    """
    raise NotImplementedError


def binary_search(arr: list, target: int) -> int:
    """
    Recherche binaire dans un tableau trié.
    Retourne l'indice de target ou -1 si absent.
    Complexité attendue : O(log n).
    TODO
    """
    raise NotImplementedError


def lower_bound(arr: list, target: int) -> int:
    """
    Premier indice i tel que arr[i] >= target.
    Retourne len(arr) si target > tous les éléments.
    Complexité attendue : O(log n).
    TODO
    """
    raise NotImplementedError


def upper_bound(arr: list, target: int) -> int:
    """
    Premier indice i tel que arr[i] > target.
    Retourne len(arr) si target >= tous les éléments.
    Complexité attendue : O(log n).
    TODO
    """
    raise NotImplementedError


def transpose(m: list) -> None:
    """
    Transposée d'une matrice n×n en place.
    Complexité attendue : O(n²).
    TODO : échanger m[i][j] et m[j][i] pour j > i
    """
    raise NotImplementedError


def rotate_90(m: list) -> None:
    """
    Rotation 90° sens horaire en place.
    Étapes : transposer, puis inverser chaque ligne.
    TODO
    """
    raise NotImplementedError


def max_subarray(arr: list) -> int:
    """
    Sous-tableau contigu de somme maximale (algorithme de Kadane).
    Complexité attendue : O(n).
    TODO : cur = max(arr[i], cur + arr[i]) ; best = max(best, cur)
    """
    raise NotImplementedError
