"""Tests pytest — TP 14 : Tas Binaires"""
import pytest, random
from tp14_tas import MinHeap, heap_sort, k_largest, TaskQueue


class TestMinHeap:
    def test_insert_extract(self):
        h = MinHeap()
        for v in [5,3,8,1,4]:
            h.insert(v)
        assert h.get_min() == 1
        assert h.extract_min() == 1
        assert h.extract_min() == 3

    def test_extract_all_ordered(self):
        h = MinHeap()
        vals = [5,3,8,1,9,2,7,4,6]
        for v in vals:
            h.insert(v)
        result = []
        while not h.is_empty():
            result.append(h.extract_min())
        assert result == sorted(vals)

    def test_build_heap(self):
        h = MinHeap()
        h.build_heap([5,3,8,1,9,2,7,4,6])
        result = []
        while not h.is_empty():
            result.append(h.extract_min())
        assert result == sorted([5,3,8,1,9,2,7,4,6])

    def test_build_heap_o_n(self):
        """build_heap doit être correct pour un grand tableau."""
        h = MinHeap()
        vals = list(range(1000, 0, -1))
        h.build_heap(vals)
        assert h.extract_min() == 1

    def test_empty_raises(self):
        h = MinHeap()
        with pytest.raises((IndexError, Exception)):
            h.extract_min()


class TestHeapSort:
    def test_basic(self):
        a = [5,2,8,1,9,3,7,4,6]
        heap_sort(a)
        assert a == [1,2,3,4,5,6,7,8,9]

    def test_empty(self):
        a = []
        heap_sort(a)
        assert a == []

    def test_single(self):
        a = [42]
        heap_sort(a)
        assert a == [42]

    def test_duplicates(self):
        a = [3,1,4,1,5,9,2,6,5]
        heap_sort(a)
        assert a == sorted([3,1,4,1,5,9,2,6,5])

    @pytest.mark.timeout(3)
    def test_large(self):
        random.seed(0)
        a = random.sample(range(10_000), 5_000)
        expected = sorted(a)
        heap_sort(a)
        assert a == expected


class TestKLargest:
    def test_basic(self):
        arr = [3,1,4,1,5,9,2,6,5,3,5]
        result = sorted(k_largest(arr, 3), reverse=True)
        assert result == [9,6,5]

    def test_k_equals_n(self):
        arr = [3,1,2]
        assert sorted(k_largest(arr, 3)) == [1,2,3]

    def test_k_one(self):
        arr = [3,1,4,1,5,9]
        assert k_largest(arr, 1) == [9]

    def test_large(self):
        arr = list(range(1000))
        result = sorted(k_largest(arr, 5), reverse=True)
        assert result == [999,998,997,996,995]


class TestTaskQueue:
    def test_order(self):
        tq = TaskQueue()
        tq.add_task("Low",    10)
        tq.add_task("High",    1)
        tq.add_task("Medium",  5)
        assert tq.next_task() == "High"
        assert tq.next_task() == "Medium"
        assert tq.next_task() == "Low"

    def test_empty_raises(self):
        with pytest.raises((IndexError, Exception)):
            TaskQueue().next_task()
