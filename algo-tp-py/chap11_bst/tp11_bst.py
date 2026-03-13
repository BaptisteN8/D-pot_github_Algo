"""TP 11 — Arbres Binaires de Recherche (BST)"""
import math


class BSTNode:
    def __init__(self, val):
        self.val   = val
        self.left  = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # ── Exercice 1 ─────────────────────────────────────────────────────────
    def insert(self, val) -> None:
        """Insère val — O(h). TODO"""
        raise NotImplementedError

    def search(self, val) -> bool:
        """Retourne True si val est présent — O(h). TODO"""
        raise NotImplementedError

    def delete(self, val) -> None:
        """
        Supprime val — O(h). Gérer les 3 cas :
        1. Feuille : supprimer directement
        2. Un enfant : remplacer par l'enfant
        3. Deux enfants : remplacer par le successeur in-ordre (min du sous-arbre droit)
        TODO
        """
        raise NotImplementedError

    def height(self) -> int:
        """Hauteur de l'arbre — O(n). TODO"""
        raise NotImplementedError

    def count_nodes(self) -> int:
        """Nombre de nœuds — O(n). TODO"""
        raise NotImplementedError

    def inorder(self) -> list:
        """Parcours in-ordre (trié) — O(n). TODO"""
        raise NotImplementedError

    def preorder(self) -> list:
        """Parcours pré-ordre — O(n). TODO"""
        raise NotImplementedError

    def postorder(self) -> list:
        """Parcours post-ordre — O(n). TODO"""
        raise NotImplementedError


# ── Exercice 2 ─────────────────────────────────────────────────────────────
def is_valid_bst(node: BSTNode | None,
                 min_val: float = -math.inf,
                 max_val: float =  math.inf) -> bool:
    """
    Vérifie la propriété BST : chaque nœud est dans (min_val, max_val).
    O(n). TODO
    """
    raise NotImplementedError


# ── Exercice 3 ─────────────────────────────────────────────────────────────
def sorted_array_to_bst(arr: list) -> BSTNode | None:
    """
    Construit un BST équilibré depuis un tableau trié.
    Le milieu du tableau est la racine.
    Hauteur résultante : ⌈log₂(n+1)⌉.
    TODO
    """
    raise NotImplementedError
