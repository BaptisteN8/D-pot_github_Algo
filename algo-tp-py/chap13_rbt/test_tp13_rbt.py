"""Tests pytest — TP 13 : Arbres Rouges et Noirs"""
import pytest
from tp13_rbt import RBTNode, RED, BLACK, is_valid_rbt


def build_valid_rbt():
    """
    Arbre RBT valide :
           13(N)
          /      \\
        8(R)     17(R)
       /  \\     /  \\
     1(N) 11(N) 15(N) 25(N)
    """
    root    = RBTNode(13, BLACK)
    root.left   = RBTNode(8,  RED)
    root.right  = RBTNode(17, RED)
    root.left.left   = RBTNode(1,  BLACK)
    root.left.right  = RBTNode(11, BLACK)
    root.right.left  = RBTNode(15, BLACK)
    root.right.right = RBTNode(25, BLACK)
    return root


class TestIsValidRBT:
    def test_none(self):
        assert is_valid_rbt(None) is True

    def test_single_black(self):
        assert is_valid_rbt(RBTNode(42, BLACK)) is True

    def test_red_root_invalid(self):
        assert is_valid_rbt(RBTNode(42, RED)) is False

    def test_valid_tree(self):
        assert is_valid_rbt(build_valid_rbt()) is True

    def test_prop4_violation(self):
        """Rouge avec enfant rouge — violation prop 4."""
        root = RBTNode(10, BLACK)
        root.left = RBTNode(5, RED)
        root.left.left = RBTNode(2, RED)   # rouge sous rouge !
        root.right = RBTNode(15, BLACK)
        assert is_valid_rbt(root) is False

    def test_prop5_violation(self):
        """Black-heights différentes — violation prop 5."""
        root = RBTNode(10, BLACK)
        root.left  = RBTNode(5,  BLACK)   # bh gauche = 2
        root.right = None                  # bh droite = 1
        assert is_valid_rbt(root) is False

    def test_prop2_violation_after_rotation(self):
        """Racine rouge."""
        root = build_valid_rbt()
        root.color = RED
        assert is_valid_rbt(root) is False

    def test_valid_minimal(self):
        """Arbre à 3 nœuds valide."""
        root = RBTNode(2, BLACK)
        root.left  = RBTNode(1, RED)
        root.right = RBTNode(3, RED)
        assert is_valid_rbt(root) is True
