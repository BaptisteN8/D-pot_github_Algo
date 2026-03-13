"""Tests pytest — TP 02 : Tableaux"""
import pytest
from tp02_tableaux import (
    rotate, remove_duplicates, merge_arrays,
    binary_search, lower_bound, upper_bound,
    transpose, rotate_90, max_subarray,
)


class TestRotate:
    def test_basic(self):
        a = [1, 2, 3, 4, 5]
        rotate(a, 2)
        assert a == [4, 5, 1, 2, 3]

    def test_k_zero(self):
        a = [1, 2, 3]
        rotate(a, 0)
        assert a == [1, 2, 3]

    def test_k_equals_len(self):
        a = [1, 2, 3]
        rotate(a, 3)
        assert a == [1, 2, 3]

    def test_k_greater_than_len(self):
        a = [1, 2, 3, 4]
        rotate(a, 6)   # 6 % 4 = 2
        assert a == [3, 4, 1, 2]

    def test_single(self):
        a = [42]
        rotate(a, 5)
        assert a == [42]


class TestRemoveDuplicates:
    def test_basic(self):
        a = [1, 1, 2, 3, 3, 3, 4]
        n = remove_duplicates(a)
        assert n == 4
        assert a[:n] == [1, 2, 3, 4]

    def test_no_duplicates(self):
        a = [1, 2, 3]
        assert remove_duplicates(a) == 3

    def test_all_same(self):
        a = [7, 7, 7, 7]
        assert remove_duplicates(a) == 1

    def test_empty(self):
        a = []
        assert remove_duplicates(a) == 0


class TestMergeArrays:
    def test_basic(self):
        assert merge_arrays([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    def test_one_empty(self):
        assert merge_arrays([], [1, 2, 3]) == [1, 2, 3]
        assert merge_arrays([1, 2, 3], []) == [1, 2, 3]

    def test_duplicates(self):
        assert merge_arrays([1, 3, 3], [2, 3, 4]) == [1, 2, 3, 3, 3, 4]

    def test_different_sizes(self):
        assert merge_arrays([1], [2, 3, 4, 5]) == [1, 2, 3, 4, 5]


class TestBinarySearch:
    def test_found(self):
        a = [1, 3, 5, 7, 9, 11]
        assert binary_search(a, 7)  == 3
        assert binary_search(a, 1)  == 0
        assert binary_search(a, 11) == 5

    def test_not_found(self):
        a = [1, 3, 5, 7, 9]
        assert binary_search(a, 6) == -1
        assert binary_search(a, 0) == -1

    def test_empty(self):
        assert binary_search([], 5) == -1

    def test_single(self):
        assert binary_search([42], 42) == 0
        assert binary_search([42], 1)  == -1


class TestBounds:
    def setup_method(self):
        self.a = [1, 3, 3, 3, 5, 7]

    def test_lower_bound_existing(self):
        assert lower_bound(self.a, 3) == 1

    def test_lower_bound_between(self):
        assert lower_bound(self.a, 4) == 4   # premier >= 4

    def test_upper_bound_existing(self):
        assert upper_bound(self.a, 3) == 4   # premier > 3

    def test_bound_past_end(self):
        assert lower_bound(self.a, 99) == len(self.a)
        assert upper_bound(self.a, 99) == len(self.a)

    def test_bound_before_start(self):
        assert lower_bound(self.a, 0) == 0
        assert upper_bound(self.a, 0) == 0


class TestMatrix:
    def test_transpose(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        transpose(m)
        assert m == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    def test_transpose_1x1(self):
        m = [[5]]
        transpose(m)
        assert m == [[5]]

    def test_rotate_90(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate_90(m)
        assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    def test_rotate_90_twice(self):
        m = [[1, 2], [3, 4]]
        rotate_90(m)
        rotate_90(m)
        assert m == [[4, 3], [2, 1]]   # 180°


class TestMaxSubarray:
    def test_mixed(self):
        assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_all_negative(self):
        assert max_subarray([-3, -1, -2]) == -1

    def test_all_positive(self):
        assert max_subarray([1, 2, 3, 4]) == 10

    def test_single(self):
        assert max_subarray([5]) == 5
        assert max_subarray([-5]) == -5

    def test_zeros(self):
        assert max_subarray([0, 0, 0]) == 0
