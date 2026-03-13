"""Tests pytest — TP 08 : Piles"""
import pytest
from tp08_piles import Stack, is_balanced, eval_rpn, MinStack, sort_stack


class TestStack:
    def test_push_pop(self):
        s = Stack()
        s.push(1); s.push(2); s.push(3)
        assert s.pop() == 3
        assert s.pop() == 2

    def test_peek(self):
        s = Stack()
        s.push(42)
        assert s.peek() == 42
        assert len(s) == 1   # peek ne dépile pas

    def test_is_empty(self):
        s = Stack()
        assert s.is_empty()
        s.push(1)
        assert not s.is_empty()
        s.pop()
        assert s.is_empty()

    def test_pop_empty_raises(self):
        with pytest.raises(IndexError):
            Stack().pop()

    def test_peek_empty_raises(self):
        with pytest.raises(IndexError):
            Stack().peek()

    def test_len(self):
        s = Stack()
        for i in range(5):
            s.push(i)
        assert len(s) == 5


class TestIsBalanced:
    def test_valid(self):
        assert is_balanced("()[]{}") is True
        assert is_balanced("{[()]}") is True
        assert is_balanced("")       is True

    def test_invalid(self):
        assert is_balanced("([)]")  is False
        assert is_balanced("{")     is False
        assert is_balanced("}")     is False

    def test_nested(self):
        assert is_balanced("(((())))")  is True
        assert is_balanced("((())")     is False

    def test_ignores_other_chars(self):
        assert is_balanced("a(b+c)*[d-e]") is True


class TestEvalRPN:
    def test_basic(self):
        assert eval_rpn(["3","4","+","2","*"]) == 14
        assert eval_rpn(["5","1","2","+","4","*","+"]) == 21

    def test_single_number(self):
        assert eval_rpn(["42"]) == 42

    def test_subtraction(self):
        assert eval_rpn(["10","3","-"]) == 7

    def test_division(self):
        assert eval_rpn(["10","3","/"]) == 3   # troncature vers 0

    def test_negative_result(self):
        assert eval_rpn(["3","5","-"]) == -2

    def test_complex(self):
        # (4+3)*(2-1) = 7
        assert eval_rpn(["4","3","+","2","1","-","*"]) == 7


class TestMinStack:
    def test_basic(self):
        ms = MinStack()
        ms.push(3); ms.push(1); ms.push(2)
        assert ms.get_min() == 1
        assert ms.top()     == 2

    def test_pop_updates_min(self):
        ms = MinStack()
        ms.push(3); ms.push(1)
        assert ms.get_min() == 1
        ms.pop()
        assert ms.get_min() == 3

    def test_duplicate_min(self):
        ms = MinStack()
        ms.push(2); ms.push(1); ms.push(1)
        assert ms.get_min() == 1
        ms.pop()
        assert ms.get_min() == 1
        ms.pop()
        assert ms.get_min() == 2

    def test_decreasing(self):
        ms = MinStack()
        for v in [5, 4, 3, 2, 1]:
            ms.push(v)
            assert ms.get_min() == v


class TestSortStack:
    def test_basic(self):
        s = Stack()
        for v in [3, 1, 4, 1, 5, 9, 2, 6]:
            s.push(v)
        sort_stack(s)
        result = []
        while not s.is_empty():
            result.append(s.pop())
        assert result == sorted([3,1,4,1,5,9,2,6])

    def test_empty(self):
        s = Stack()
        sort_stack(s)
        assert s.is_empty()

    def test_single(self):
        s = Stack()
        s.push(42)
        sort_stack(s)
        assert s.pop() == 42
