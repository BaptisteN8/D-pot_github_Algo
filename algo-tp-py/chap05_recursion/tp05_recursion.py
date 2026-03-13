"""
TP 05 — La Récursion
"""


def power(x: float, n: int) -> float:
    """
    x^n en O(log n) — exponentiation rapide.
    Si n pair : (x^(n//2))^2 ; si impair : x * x^(n-1).
    TODO
    """
    raise NotImplementedError


def gcd(a: int, b: int) -> int:
    """
    PGCD par algorithme d'Euclide récursif.
    gcd(a, b) = gcd(b, a % b) ; gcd(a, 0) = a.
    TODO
    """
    raise NotImplementedError


def is_palindrome(s: str, l: int, r: int) -> bool:
    """
    True si s[l..r] est un palindrome (récursif).
    Cas de base : l >= r → True.
    TODO
    """
    raise NotImplementedError


def hanoi(n: int, from_: str, to: str, via: str) -> list[tuple]:
    """
    Retourne la liste des mouvements pour résoudre les Tours de Hanoï.
    Chaque mouvement est (from_, to).
    Complexité : O(2^n) mouvements.
    TODO
    """
    raise NotImplementedError


# compteur global pour mesurer les appels
_call_count = 0

def fib_naive(n: int) -> int:
    """Fibonacci naïf — O(2^n). Incrémente _call_count à chaque appel."""
    global _call_count
    _call_count += 1
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n: int, memo: dict = None) -> int:
    """
    Fibonacci avec mémoïsation — O(n).
    TODO : if n in memo: return memo[n] ; memo[n] = fib_memo(n-1)+fib_memo(n-2)
    """
    raise NotImplementedError


def permutations(arr: list) -> list[list]:
    """
    Retourne toutes les permutations de arr (backtracking).
    Complexité : O(n! * n).
    TODO
    """
    raise NotImplementedError


def subsets(arr: list) -> list[list]:
    """
    Retourne tous les sous-ensembles de arr (2^n au total).
    TODO : récursion — sans arr[idx] puis avec arr[idx]
    """
    raise NotImplementedError
