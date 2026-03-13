"""Tests pytest — TP 11 : Arbres BST"""
import pytest, math
from tp11_bst import BST, BSTNode, is_valid_bst, sorted_array_to_bst


class TestBST:
    def _build(self):
        t = BST()
        for v in [5,3,7,1,4,6,8]:
            t.insert(v)
        return t

    def test_search(self):
        t = self._build()
        assert t.search(4) is True
        assert t.search(9) is False

    def test_inorder_sorted(self):
        t = self._build()
        s = t.inorder()
        assert s == sorted(s) and len(s) == 7

    def test_height(self):
        t = self._build()
        assert t.height() == 2

    def test_count_nodes(self):
        assert self._build().count_nodes() == 7

    def test_delete_leaf(self):
        t = self._build()
        t.delete(1)
        assert t.search(1) is False
        assert t.count_nodes() == 6
        assert t.inorder() == sorted([5,3,7,4,6,8])

    def test_delete_one_child(self):
        t = self._build()
        t.delete(6)
        assert t.search(6) is False
        assert is_valid_bst(t.root)

    def test_delete_two_children(self):
        t = self._build()
        t.delete(3)
        assert t.search(3) is False
        s = t.inorder()
        assert s == sorted(s)

    def test_delete_root(self):
        t = self._build()
        t.delete(5)
        assert t.search(5) is False
        s = t.inorder()
        assert s == sorted(s)

    def test_delete_nonexistent(self):
        t = self._build()
        t.delete(99)   # ne doit pas lever d'exception
        assert t.count_nodes() == 7

    def test_preorder_postorder(self):
        t = self._build()
        pre  = t.preorder()
        post = t.postorder()
        assert pre[0]  == 5   # racine en premier
        assert post[-1] == 5  # racine en dernier
        assert set(pre) == set(post)


class TestIsValidBST:
    def test_valid(self):
        t = BST()
        for v in [5,3,7,1,4,6,8]:
            t.insert(v)
        assert is_valid_bst(t.root) is True

    def test_none(self):
        assert is_valid_bst(None) is True

    def test_invalid_left_greater(self):
        n = BSTNode(5)
        n.left = BSTNode(10)   # violation
        assert is_valid_bst(n) is False

    def test_invalid_deep(self):
        # Arbre qui semble correct localement mais viole BST en profondeur
        root = BSTNode(10)
        root.left = BSTNode(5)
        root.left.right = BSTNode(15)   # 15 > 10, violation
        assert is_valid_bst(root) is False


class TestSortedArrayToBST:
    def test_inorder_equals_input(self):
        arr = [1,2,3,4,5,6,7]
        root = sorted_array_to_bst(arr)
        t = BST(); t.root = root
        assert t.inorder() == arr

    def test_balanced_height(self):
        for n in [7, 15, 31, 63]:
            arr = list(range(n))
            root = sorted_array_to_bst(arr)
            t = BST(); t.root = root
            expected_max = math.ceil(math.log2(n + 1))
            assert t.height() <= expected_max

    def test_valid_bst(self):
        arr = list(range(10))
        root = sorted_array_to_bst(arr)
        assert is_valid_bst(root)

    def test_empty(self):
        assert sorted_array_to_bst([]) is None

    def test_single(self):
        root = sorted_array_to_bst([42])
        assert root.val == 42
