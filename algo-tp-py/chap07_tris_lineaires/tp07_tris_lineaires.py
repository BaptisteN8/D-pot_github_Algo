"""TP 07 — Les Tris Linéaires"""


def counting_sort(arr: list, k: int) -> list:
    """
    Tri par dénombrement stable pour des entiers dans [0, k].
    Complexité : O(n+k) temps et espace.
    TODO :
    1. count[0..k] = 0
    2. count[arr[i]] += 1 pour tout i
    3. prefix sum : count[i] += count[i-1]
    4. de droite à gauche : output[--count[arr[i]]] = arr[i]
    """
    raise NotImplementedError


def count_sort_by_digit(arr: list, exp: int) -> None:
    """
    Counting sort stable sur le chiffre de rang exp (base 10), en place.
    TODO
    """
    raise NotImplementedError


def radix_sort(arr: list) -> None:
    """
    Radix Sort LSD pour entiers positifs — en place.
    Complexité : O(d*(n+10)) où d = nombre de chiffres du max.
    TODO : for exp=1, 10, 100... tant que max//exp > 0
    """
    raise NotImplementedError


def bucket_sort(arr: list) -> None:
    """
    Bucket Sort pour flottants dans [0.0, 1.0) — en place.
    Complexité : O(n) moyen.
    TODO :
    1. n buckets
    2. distribuer arr[i] dans bucket[int(n * arr[i])]
    3. trier chaque bucket (insertion sort ou sorted)
    4. concaténer
    """
    raise NotImplementedError
