"""Tests pytest — TP 09 : Files"""
import pytest
from tp09_files import CircularQueue, MinPriorityQueue, bfs, shortest_path, TreeNode, level_order


class TestCircularQueue:
    def test_enqueue_dequeue(self):
        q = CircularQueue(4)
        q.enqueue(1); q.enqueue(2); q.enqueue(3)
        assert q.front() == 1
        assert q.dequeue() == 1
        assert len(q) == 2

    def test_circular(self):
        q = CircularQueue(3)
        q.enqueue(1); q.enqueue(2); q.enqueue(3)
        q.dequeue()
        q.enqueue(4)
        assert q.front() == 2
        assert len(q) == 3

    def test_full_raises(self):
        q = CircularQueue(2)
        q.enqueue(1); q.enqueue(2)
        with pytest.raises(OverflowError):
            q.enqueue(3)

    def test_empty_raises(self):
        q = CircularQueue(2)
        with pytest.raises(IndexError):
            q.dequeue()

    def test_fifo_order(self):
        q = CircularQueue(10)
        for v in range(5):
            q.enqueue(v)
        result = []
        while not q.is_empty():
            result.append(q.dequeue())
        assert result == list(range(5))


class TestMinPQ:
    def test_insert_extract(self):
        pq = MinPriorityQueue()
        pq.insert("C", 3); pq.insert("A", 1); pq.insert("B", 2)
        assert pq.extract_min() == "A"
        assert pq.extract_min() == "B"
        assert pq.extract_min() == "C"

    def test_peek(self):
        pq = MinPriorityQueue()
        pq.insert("X", 5); pq.insert("Y", 1)
        assert pq.peek_min() == "Y"
        assert len(pq) == 2

    def test_heap_property(self):
        import random
        pq = MinPriorityQueue()
        vals = [(random.randint(0,100), i) for i in range(20)]
        for v, p in vals:
            pq.insert(v, p)
        prev_p = -1
        while len(pq) > 0:
            pq.extract_min()  # doit ne pas lever d'exception


class TestBFS:
    def test_basic(self):
        adj = [[1,2],[0,3],[0,3],[1,2]]
        order = bfs(adj, 0)
        assert order[0] == 0
        assert set(order) == {0,1,2,3}

    def test_disconnected(self):
        adj = [[1],[0],[3],[2]]
        order = bfs(adj, 0)
        assert set(order) == {0,1}   # 2 et 3 non connexes

    def test_single(self):
        assert bfs([[]], 0) == [0]


class TestShortestPath:
    def test_direct(self):
        adj = [[1,2],[0,3],[0,3],[1,2]]
        assert shortest_path(adj, 0, 1) == 1

    def test_two_hops(self):
        adj = [[1],[0,2],[1,3],[2]]
        assert shortest_path(adj, 0, 3) == 3

    def test_same_node(self):
        adj = [[1],[0]]
        assert shortest_path(adj, 0, 0) == 0

    def test_unreachable(self):
        adj = [[1],[0],[3],[2]]
        assert shortest_path(adj, 0, 2) == -1


class TestLevelOrder:
    def _build(self):
        r = TreeNode(3)
        r.left  = TreeNode(9)
        r.right = TreeNode(20)
        r.right.left  = TreeNode(15)
        r.right.right = TreeNode(7)
        return r

    def test_basic(self):
        result = level_order(self._build())
        assert result == [[3],[9,20],[15,7]]

    def test_none(self):
        assert level_order(None) == []

    def test_single(self):
        assert level_order(TreeNode(42)) == [[42]]

    def test_complete(self):
        r = TreeNode(1)
        r.left = TreeNode(2); r.right = TreeNode(3)
        r.left.left = TreeNode(4); r.left.right = TreeNode(5)
        assert level_order(r) == [[1],[2,3],[4,5]]
