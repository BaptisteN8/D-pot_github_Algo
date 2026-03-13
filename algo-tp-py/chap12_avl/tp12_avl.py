"""TP 12 — Arbres AVL"""


class AVLNode:
    def __init__(self, val):
        self.val    = val
        self.height = 1
        self.left   = None
        self.right  = None


def _h(n):  return n.height if n else 0
def _bf(n): return _h(n.right) - _h(n.left) if n else 0
def _uh(n):
    if n: n.height = 1 + max(_h(n.left), _h(n.right))


def rotate_right(z: AVLNode) -> AVLNode:
    """
    Rotation droite autour de z (cas LL).
    y = z.left ; z.left = y.right ; y.right = z
    Mettre à jour les hauteurs, retourner y.
    TODO
    """
    raise NotImplementedError


def rotate_left(z: AVLNode) -> AVLNode:
    """Rotation gauche autour de z (cas RR). TODO"""
    raise NotImplementedError


def balance(node: AVLNode) -> AVLNode:
    """
    Rééquilibre node si nécessaire (4 cas).
    Met à jour la hauteur, retourne la nouvelle racine.
    TODO
    """
    raise NotImplementedError


def avl_insert(root: AVLNode | None, val: int) -> AVLNode:
    """
    Insère val dans l'AVL, retourne la nouvelle racine.
    BST insert + balance(). TODO
    """
    raise NotImplementedError


def is_avl(node: AVLNode | None) -> bool:
    """
    Retourne True si le sous-arbre respecte la propriété AVL.
    Balance factor ∈ {-1, 0, +1} pour chaque nœud. TODO
    """
    raise NotImplementedError


def avl_inorder(node: AVLNode | None) -> list:
    if not node: return []
    return avl_inorder(node.left) + [node.val] + avl_inorder(node.right)
