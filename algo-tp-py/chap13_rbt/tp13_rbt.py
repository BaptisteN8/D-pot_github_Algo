"""TP 13 — Arbres Rouges et Noirs"""

RED   = 0
BLACK = 1


class RBTNode:
    def __init__(self, val, color=RED):
        self.val    = val
        self.color  = color
        self.left   = None
        self.right  = None
        self.parent = None


def check_bh(node: RBTNode | None) -> int:
    """
    Retourne la black-height du sous-arbre ou -1 si une propriété est violée.
    None (feuille) compte pour black-height = 1.

    Propriétés à vérifier :
    - Prop 4 : un nœud rouge n'a pas d'enfant rouge
    - Prop 5 : black-height identique dans les deux sous-arbres

    TODO
    """
    raise NotImplementedError


def is_valid_rbt(root: RBTNode | None) -> bool:
    """
    Retourne True si root est un RBT valide.
    Vérifie aussi la prop 2 (racine noire).
    TODO
    """
    raise NotImplementedError
