"""Tests pytest — TP 12 : Arbres AVL"""
import pytest
from tp12_avl import AVLNode, rotate_right, rotate_left, avl_insert, is_avl, avl_inorder, _h


class TestRotations:
    def test_rotate_right(self):
        z = AVLNode(3); y = AVLNode(2); x = AVLNode(1)
        z.left = y; y.left = x
        y.height = 2; z.height = 3
        new_root = rotate_right(z)
        assert new_root.val == 2
        assert new_root.right.val == 3
        assert new_root.left.val  == 1

    def test_rotate_left(self):
        z = AVLNode(1); y = AVLNode(2); x = AVLNode(3)
        z.right = y; y.right = x
        y.height = 2; z.height = 3
        new_root = rotate_left(z)
        assert new_root.val == 2
        assert new_root.left.val  == 1
        assert new_root.right.val == 3


class TestAVLInsert:
    def test_ll_rotation(self):
        root = None
        for v in [3, 2, 1]:
            root = avl_insert(root, v)
        assert is_avl(root)
        assert root.val == 2

    def test_rr_rotation(self):
        root = None
        for v in [1, 2, 3]:
            root = avl_insert(root, v)
        assert is_avl(root)
        assert root.val == 2

    def test_lr_rotation(self):
        root = None
        for v in [3, 1, 2]:
            root = avl_insert(root, v)
        assert is_avl(root)
        assert root.val == 2

    def test_rl_rotation(self):
        root = None
        for v in [1, 3, 2]:
            root = avl_insert(root, v)
        assert is_avl(root)
        assert root.val == 2

    def test_inorder_sorted(self):
        root = None
        import random; random.seed(0)
        vals = random.sample(range(100), 20)
        for v in vals:
            root = avl_insert(root, v)
        assert avl_inorder(root) == sorted(vals)

    def test_height_bounded(self):
        import math
        root = None
        for i in range(1, 101):
            root = avl_insert(root, i)
        assert is_avl(root)
        assert _h(root) <= 2 * math.log2(101)

    def test_bst_degenerate_comparison(self):
        """BST sur 1..20 croissant → hauteur 19 ; AVL → hauteur ≤ 5"""
        root = None
        for i in range(1, 21):
            root = avl_insert(root, i)
        assert is_avl(root)
        assert _h(root) <= 5
