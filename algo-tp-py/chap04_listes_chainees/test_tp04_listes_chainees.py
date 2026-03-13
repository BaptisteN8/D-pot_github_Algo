"""Tests pytest — TP 04 : Listes Doublement Chaînées"""
import pytest
from tp04_listes_chainees import DoublyLinkedList, Node, reverse_iterative, SNode, has_cycle, kth_from_end


class TestDoublyLinkedList:
    def test_push_back_and_iter(self):
        lst = DoublyLinkedList()
        for v in [1, 2, 3]:
            lst.push_back(v)
        assert lst.to_list() == [1, 2, 3]

    def test_push_front(self):
        lst = DoublyLinkedList()
        for v in [1, 2, 3]:
            lst.push_front(v)
        assert lst.to_list() == [3, 2, 1]

    def test_len(self):
        lst = DoublyLinkedList()
        assert len(lst) == 0
        lst.push_back(1); lst.push_back(2)
        assert len(lst) == 2

    def test_head_tail_after_push(self):
        lst = DoublyLinkedList()
        lst.push_back(10); lst.push_back(20); lst.push_back(30)
        assert lst.head.data == 10
        assert lst.tail.data == 30

    def test_pop_front(self):
        lst = DoublyLinkedList()
        for v in [1, 2, 3]:
            lst.push_back(v)
        assert lst.pop_front() == 1
        assert lst.to_list() == [2, 3]
        assert len(lst) == 2

    def test_pop_back(self):
        lst = DoublyLinkedList()
        for v in [1, 2, 3]:
            lst.push_back(v)
        assert lst.pop_back() == 3
        assert lst.to_list() == [1, 2]

    def test_pop_until_empty(self):
        lst = DoublyLinkedList()
        lst.push_back(42)
        assert lst.pop_front() == 42
        assert len(lst) == 0
        assert lst.head is None and lst.tail is None

    def test_pop_empty_raises(self):
        lst = DoublyLinkedList()
        with pytest.raises(IndexError):
            lst.pop_front()
        with pytest.raises(IndexError):
            lst.pop_back()

    def test_find(self):
        lst = DoublyLinkedList()
        for v in [10, 20, 30]:
            lst.push_back(v)
        n = lst.find(20)
        assert n is not None and n.data == 20
        assert lst.find(99) is None

    def test_insert_after(self):
        lst = DoublyLinkedList()
        lst.push_back(1); lst.push_back(3)
        n1 = lst.find(1)
        lst.insert_after(n1, 2)
        assert lst.to_list() == [1, 2, 3]

    def test_insert_after_tail(self):
        lst = DoublyLinkedList()
        lst.push_back(1)
        n = lst.tail
        lst.insert_after(n, 2)
        assert lst.tail.data == 2
        assert lst.to_list() == [1, 2]

    def test_remove_middle(self):
        lst = DoublyLinkedList()
        for v in [1, 2, 3]:
            lst.push_back(v)
        n2 = lst.find(2)
        lst.remove(n2)
        assert lst.to_list() == [1, 3]

    def test_remove_head(self):
        lst = DoublyLinkedList()
        for v in [1, 2, 3]:
            lst.push_back(v)
        lst.remove(lst.head)
        assert lst.to_list() == [2, 3]
        assert lst.head.data == 2

    def test_remove_tail(self):
        lst = DoublyLinkedList()
        for v in [1, 2, 3]:
            lst.push_back(v)
        lst.remove(lst.tail)
        assert lst.to_list() == [1, 2]
        assert lst.tail.data == 2

    def test_prev_links(self):
        """Vérifie que les liens prev sont corrects."""
        lst = DoublyLinkedList()
        for v in [1, 2, 3]:
            lst.push_back(v)
        cur = lst.tail
        backward = []
        while cur:
            backward.append(cur.data)
            cur = cur.prev
        assert backward == [3, 2, 1]


class TestReverseIterative:
    def test_basic(self):
        lst = DoublyLinkedList()
        for v in [1, 2, 3, 4, 5]:
            lst.push_back(v)
        reverse_iterative(lst)
        assert lst.to_list() == [5, 4, 3, 2, 1]
        assert lst.head.data == 5
        assert lst.tail.data == 1

    def test_single(self):
        lst = DoublyLinkedList()
        lst.push_back(42)
        reverse_iterative(lst)
        assert lst.to_list() == [42]

    def test_empty(self):
        lst = DoublyLinkedList()
        reverse_iterative(lst)
        assert lst.to_list() == []

    def test_prev_links_after_reverse(self):
        lst = DoublyLinkedList()
        for v in [1, 2, 3]:
            lst.push_back(v)
        reverse_iterative(lst)
        cur = lst.tail
        backward = []
        while cur:
            backward.append(cur.data)
            cur = cur.prev
        assert backward == [1, 2, 3]


class TestHasCycle:
    def _build_list(self, values):
        if not values:
            return None
        nodes = [SNode(v) for v in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]
        return nodes[0], nodes

    def test_no_cycle(self):
        head, _ = self._build_list([1, 2, 3, 4])
        assert has_cycle(head) is False

    def test_with_cycle(self):
        head, nodes = self._build_list([1, 2, 3, 4])
        nodes[-1].next = nodes[1]   # cycle vers nœud 2
        assert has_cycle(head) is True

    def test_self_loop(self):
        head, nodes = self._build_list([1])
        nodes[0].next = nodes[0]
        assert has_cycle(head) is True

    def test_none(self):
        assert has_cycle(None) is False


class TestKthFromEnd:
    def _build_list(self, values):
        if not values:
            return None
        nodes = [SNode(v) for v in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]
        return nodes[0]

    def test_last(self):
        assert kth_from_end(self._build_list([10, 20, 30, 40, 50]), 1) == 50

    def test_third_from_end(self):
        assert kth_from_end(self._build_list([10, 20, 30, 40, 50]), 3) == 30

    def test_first(self):
        assert kth_from_end(self._build_list([10, 20, 30]), 3) == 10

    def test_single_element(self):
        assert kth_from_end(self._build_list([99]), 1) == 99

    def test_invalid_k(self):
        with pytest.raises((ValueError, IndexError)):
            kth_from_end(self._build_list([1, 2, 3]), 5)
