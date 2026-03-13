"""Tests pytest — TP 07 : Tris Linéaires"""
import pytest, random
from tp07_tris_lineaires import counting_sort, radix_sort, bucket_sort


def is_sorted(a): return all(a[i] <= a[i+1] for i in range(len(a)-1))


class TestCountingSort:
    def test_basic(self):
        result = counting_sort([4,2,2,8,3,3,1], 9)
        assert result == [1,2,2,3,3,4,8]

    def test_already_sorted(self):
        assert counting_sort([1,2,3], 5) == [1,2,3]

    def test_all_zeros(self):
        assert counting_sort([0,0,0], 0) == [0,0,0]

    def test_stable(self):
        """Vérification de stabilité basique : les éléments égaux sont préservés."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = counting_sort(arr, 9)
        assert result == sorted(arr)

    def test_empty(self):
        assert counting_sort([], 9) == []

    @pytest.mark.timeout(2)
    def test_large(self):
        random.seed(0)
        a = [random.randint(0,255) for _ in range(50_000)]
        assert counting_sort(a, 255) == sorted(a)


class TestRadixSort:
    def test_basic(self):
        a = [170,45,75,90,802,24,2,66]
        radix_sort(a)
        assert a == sorted([170,45,75,90,802,24,2,66])

    def test_single_digits(self):
        a = [5,3,8,1,9,2]
        radix_sort(a)
        assert is_sorted(a)

    def test_large_numbers(self):
        a = [999999,1,123456,42,0,100000]
        radix_sort(a)
        assert is_sorted(a)

    def test_zeros(self):
        a = [0,0,0]
        radix_sort(a)
        assert a == [0,0,0]

    @pytest.mark.timeout(2)
    def test_large(self):
        random.seed(1)
        a = [random.randint(0,10**6) for _ in range(20_000)]
        expected = sorted(a)
        radix_sort(a)
        assert a == expected


class TestBucketSort:
    def test_basic(self):
        a = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21]
        bucket_sort(a)
        assert is_sorted(a)

    def test_empty(self):
        a = []
        bucket_sort(a)
        assert a == []

    def test_single(self):
        a = [0.5]
        bucket_sort(a)
        assert a == [0.5]

    def test_all_same(self):
        a = [0.5, 0.5, 0.5]
        bucket_sort(a)
        assert a == [0.5, 0.5, 0.5]

    @pytest.mark.timeout(2)
    def test_large(self):
        import random as rnd
        rnd.seed(2)
        a = [rnd.random() for _ in range(10_000)]
        bucket_sort(a)
        assert is_sorted(a)
