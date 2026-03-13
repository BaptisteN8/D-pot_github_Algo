"""Tests pytest — TP 03 : Tris Simples"""
import pytest
import random
import time
from tp03_tris_simples import (
    bubble_sort, selection_sort, insertion_sort, insertion_sort_generic,
)


def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


# ── Tests communs aux trois tris ───────────────────────────────────────────────
@pytest.mark.parametrize("sort_fn", [bubble_sort, selection_sort, insertion_sort])
class TestTrisCommuns:
    def test_random(self, sort_fn):
        a = [5, 2, 8, 1, 9, 3, 7, 4, 6]
        sort_fn(a)
        assert is_sorted(a)

    def test_empty(self, sort_fn):
        a = []
        sort_fn(a)
        assert a == []

    def test_single(self, sort_fn):
        a = [42]
        sort_fn(a)
        assert a == [42]

    def test_already_sorted(self, sort_fn):
        a = [1, 2, 3, 4, 5]
        sort_fn(a)
        assert a == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self, sort_fn):
        a = [5, 4, 3, 2, 1]
        sort_fn(a)
        assert a == [1, 2, 3, 4, 5]

    def test_duplicates(self, sort_fn):
        a = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        sort_fn(a)
        assert is_sorted(a)

    def test_large_random(self, sort_fn):
        random.seed(0)
        a = random.sample(range(500), 300)
        sort_fn(a)
        assert is_sorted(a)


# ── Stabilité ─────────────────────────────────────────────────────────────────
class TestStabilite:
    """
    Un tri stable préserve l'ordre des éléments égaux.
    On représente les éléments par (valeur, indice_original).
    """
    def _tagged(self, values):
        return [(v, i) for i, v in enumerate(values)]

    def _check_stable(self, arr):
        for i in range(len(arr) - 1):
            if arr[i][0] == arr[i+1][0]:
                assert arr[i][1] < arr[i+1][1], "Tri non stable"

    def test_bubble_sort_stable(self):
        a = self._tagged([3, 1, 4, 1, 5, 9, 2, 6])
        bubble_sort(a)
        self._check_stable(a)

    def test_insertion_sort_stable(self):
        a = self._tagged([3, 1, 4, 1, 5, 9, 2, 6])
        insertion_sort(a)
        self._check_stable(a)


# ── insertion_sort_generic ────────────────────────────────────────────────────
class TestInsertionSortGeneric:
    def test_strings_alphabetical(self):
        a = ["banane", "apple", "cerise", "datte"]
        insertion_sort_generic(a)
        assert a == ["apple", "banane", "cerise", "datte"]

    def test_reverse(self):
        a = [3, 1, 4, 1, 5, 9]
        insertion_sort_generic(a, reverse=True)
        assert a == [9, 5, 4, 3, 1, 1]

    def test_key_function(self):
        a = ["banana", "fig", "apple", "date"]
        insertion_sort_generic(a, key=len)
        assert a == ["fig", "date", "apple", "banana"]

    def test_structs(self):
        students = [{"name": "Bob", "grade": 12},
                    {"name": "Alice", "grade": 15},
                    {"name": "Carol", "grade": 10}]
        insertion_sort_generic(students, key=lambda s: s["grade"])
        assert [s["name"] for s in students] == ["Carol", "Bob", "Alice"]


# ── Bubble sort : optimisation swapped ────────────────────────────────────────
class TestBubbleSortOptimisation:
    @pytest.mark.timeout(1)
    def test_already_sorted_fast(self):
        """Sur tableau trié, bubble_sort doit terminer en O(n), pas O(n²)."""
        a = list(range(10_000))
        t0 = time.perf_counter()
        bubble_sort(a)
        elapsed = time.perf_counter() - t0
        assert is_sorted(a)
        assert elapsed < 0.5, "bubble_sort sur tableau trié trop lent — vérifiez le flag swapped"
