"""Tests pytest — TP 01 : Complexité & Benchmarks"""
import pytest
import random
from tp01_introduction import func_a, func_b, find_pair_naive, find_pair_fast


# ── func_a ─────────────────────────────────────────────────────────────────────
class TestFuncA:
    def test_base_cases(self):
        assert func_a(1) == 1
        assert func_a(2) == 3    # (0,0),(0,1),(1,1)
        assert func_a(3) == 6    # 3+2+1

    def test_formula(self):
        # func_a(n) == n*(n+1)//2
        for n in [4, 5, 10, 20]:
            assert func_a(n) == n * (n + 1) // 2

    def test_zero(self):
        assert func_a(0) == 0


# ── func_b ─────────────────────────────────────────────────────────────────────
class TestFuncB:
    def test_powers_of_two(self):
        assert func_b(1) == 0
        assert func_b(2) == 1
        assert func_b(4) == 2
        assert func_b(8) == 3
        assert func_b(16) == 4

    def test_non_powers(self):
        assert func_b(3) == 2    # i=1→2→4 : 2 itérations
        assert func_b(10) == 4


# ── find_pair_naive ────────────────────────────────────────────────────────────
class TestFindPairNaive:
    def test_found(self):
        assert find_pair_naive([2, 7, 11, 15], 9) is True

    def test_not_found(self):
        assert find_pair_naive([2, 7, 11, 15], 20) is False

    def test_single_element(self):
        assert find_pair_naive([5], 10) is False

    def test_same_element_not_counted_twice(self):
        # [3] ne peut pas faire 3+3 avec un seul élément
        assert find_pair_naive([3, 1, 2], 6) is False

    def test_duplicates(self):
        # [3, 3] → 3+3 = 6 ✓ (deux éléments distincts)
        assert find_pair_naive([3, 3, 1], 6) is True

    def test_empty(self):
        assert find_pair_naive([], 5) is False

    def test_large(self):
        arr = list(range(100))
        assert find_pair_naive(arr, 197) is True   # 98+99
        assert find_pair_naive(arr, 200) is False


# ── find_pair_fast ─────────────────────────────────────────────────────────────
class TestFindPairFast:
    def test_found(self):
        assert find_pair_fast([2, 7, 11, 15], 9) is True

    def test_not_found(self):
        assert find_pair_fast([2, 7, 11, 15], 20) is False

    def test_same_element_not_counted_twice(self):
        assert find_pair_fast([3, 1, 2], 6) is False

    def test_duplicates(self):
        assert find_pair_fast([3, 3, 1], 6) is True

    def test_empty(self):
        assert find_pair_fast([], 5) is False

    def test_consistency_with_naive(self):
        """find_pair_fast doit donner le même résultat que find_pair_naive."""
        random.seed(42)
        for _ in range(50):
            arr = random.sample(range(500), 30)
            t = random.randint(0, 1000)
            assert find_pair_fast(arr, t) == find_pair_naive(arr, t)

    @pytest.mark.timeout(2)
    def test_performance(self):
        """find_pair_fast doit gérer 50 000 éléments rapidement."""
        arr = list(range(50_000))
        assert find_pair_fast(arr, 99_997) is True
