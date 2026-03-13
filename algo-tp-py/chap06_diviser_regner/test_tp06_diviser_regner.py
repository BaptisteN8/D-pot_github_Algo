"""Tests pytest — TP 06 : Diviser pour Régner"""
import pytest
import random
from tp06_diviser_regner import (
    merge, merge_sort, quick_sort, quick_select, count_inversions,
)


class TestMerge:
    def test_basic(self):
        assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    def test_empty(self):
        assert merge([], [1, 2]) == [1, 2]
        assert merge([1, 2], []) == [1, 2]

    def test_duplicates(self):
        assert merge([1, 3, 3], [2, 3, 4]) == [1, 2, 3, 3, 3, 4]

    def test_stability(self):
        """Les éléments de left doivent précéder ceux de right en cas d'égalité."""
        left  = [(1, 'L1'), (3, 'L2')]
        right = [(1, 'R1'), (2, 'R2')]
        result = merge(left, right)
        # Les deux (1,...) : L1 avant R1
        ones = [x for x in result if x[0] == 1]
        assert ones[0][1] == 'L1'


class TestMergeSort:
    def test_basic(self):
        assert merge_sort([5, 2, 8, 1, 9, 3]) == [1, 2, 3, 5, 8, 9]

    def test_empty(self):
        assert merge_sort([]) == []

    def test_single(self):
        assert merge_sort([42]) == [42]

    def test_already_sorted(self):
        a = list(range(10))
        assert merge_sort(a) == a

    def test_does_not_modify_input(self):
        a = [3, 1, 2]
        original = a[:]
        merge_sort(a)
        assert a == original   # ne doit pas modifier en place

    @pytest.mark.timeout(3)
    def test_large(self):
        random.seed(1)
        a = random.sample(range(10_000), 5_000)
        result = merge_sort(a)
        assert result == sorted(a)


class TestQuickSort:
    def test_basic(self):
        a = [5, 2, 8, 1, 9, 3]
        quick_sort(a)
        assert a == [1, 2, 3, 5, 8, 9]

    def test_empty(self):
        a = []
        quick_sort(a)
        assert a == []

    def test_single(self):
        a = [42]
        quick_sort(a)
        assert a == [42]

    def test_duplicates(self):
        a = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        quick_sort(a)
        assert a == sorted([3, 1, 4, 1, 5, 9, 2, 6, 5])

    @pytest.mark.timeout(3)
    def test_large(self):
        random.seed(2)
        a = random.sample(range(20_000), 5_000)
        expected = sorted(a)
        quick_sort(a)
        assert a == expected


class TestQuickSelect:
    def test_min(self):
        a = [3, 1, 4, 1, 5, 9, 2, 6]
        assert quick_select(a[:], 0, len(a)-1, 0) == 1

    def test_max(self):
        a = [3, 1, 4, 1, 5, 9, 2, 6]
        assert quick_select(a[:], 0, len(a)-1, len(a)-1) == 9

    def test_median(self):
        a = list(range(1, 10))   # [1..9]
        assert quick_select(a[:], 0, len(a)-1, 4) == 5

    def test_consistent(self):
        random.seed(3)
        a = random.sample(range(100), 20)
        for k in range(len(a)):
            assert quick_select(a[:], 0, len(a)-1, k) == sorted(a)[k]


class TestCountInversions:
    def test_no_inversions(self):
        _, cnt = count_inversions([1, 2, 3, 4, 5])
        assert cnt == 0

    def test_all_inversions(self):
        _, cnt = count_inversions([5, 4, 3, 2, 1])
        assert cnt == 10   # n*(n-1)//2

    def test_partial(self):
        _, cnt = count_inversions([2, 4, 1, 3, 5])
        assert cnt == 3

    def test_returns_sorted(self):
        sorted_arr, _ = count_inversions([3, 1, 2])
        assert sorted_arr == [1, 2, 3]

    def test_single(self):
        _, cnt = count_inversions([42])
        assert cnt == 0
