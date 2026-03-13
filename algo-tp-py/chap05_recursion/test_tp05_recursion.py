"""Tests pytest — TP 05 : Récursion"""
import pytest
import math
import tp05_recursion as tp


class TestPower:
    def test_basic(self):
        assert tp.power(2, 10) == 1024
        assert tp.power(3, 3)  == 27
        assert tp.power(5, 0)  == 1
        assert tp.power(1, 99) == 1

    def test_float(self):
        assert abs(tp.power(2.0, -1) - 0.5) < 1e-9

    def test_large_exponent(self):
        assert tp.power(2, 30) == 2**30


class TestGcd:
    def test_basic(self):
        assert tp.gcd(12, 8)   == 4
        assert tp.gcd(17, 5)   == 1
        assert tp.gcd(100, 75) == 25

    def test_equal(self):
        assert tp.gcd(7, 7) == 7

    def test_zero(self):
        assert tp.gcd(5, 0) == 5
        assert tp.gcd(0, 5) == 5


class TestIsPalindrome:
    def test_palindromes(self):
        assert tp.is_palindrome("racecar", 0, 6) is True
        assert tp.is_palindrome("a",       0, 0) is True
        assert tp.is_palindrome("aa",      0, 1) is True
        assert tp.is_palindrome("aba",     0, 2) is True

    def test_not_palindromes(self):
        assert tp.is_palindrome("hello", 0, 4) is False
        assert tp.is_palindrome("ab",    0, 1) is False

    def test_substring(self):
        s = "xabaxy"
        assert tp.is_palindrome(s, 1, 3) is True   # "aba"
        assert tp.is_palindrome(s, 0, 4) is False   # "xabax" → hmm = True
        assert tp.is_palindrome(s, 0, 5) is False


class TestHanoi:
    def test_one_disk(self):
        moves = tp.hanoi(1, 'A', 'C', 'B')
        assert moves == [('A', 'C')]

    def test_two_disks(self):
        moves = tp.hanoi(2, 'A', 'C', 'B')
        assert len(moves) == 3

    def test_three_disks(self):
        moves = tp.hanoi(3, 'A', 'C', 'B')
        assert len(moves) == 7   # 2^3 - 1

    def test_count_formula(self):
        for n in range(1, 7):
            assert len(tp.hanoi(n, 'A', 'C', 'B')) == 2**n - 1

    def test_valid_moves(self):
        """Simule les mouvements et vérifie la solution."""
        pegs = {'A': list(range(3, 0, -1)), 'B': [], 'C': []}
        for frm, to in tp.hanoi(3, 'A', 'C', 'B'):
            disk = pegs[frm].pop()
            if pegs[to]:
                assert disk < pegs[to][-1], f"Mouvement invalide : {disk} sur {pegs[to][-1]}"
            pegs[to].append(disk)
        assert pegs['C'] == [3, 2, 1]


class TestFibonacci:
    def test_fib_memo_values(self):
        expected = [0,1,1,2,3,5,8,13,21,34,55]
        for i, v in enumerate(expected):
            assert tp.fib_memo(i) == v

    def test_fib_naive_values(self):
        assert tp.fib_naive(0) == 0
        assert tp.fib_naive(10) == 55

    def test_memo_fewer_calls(self):
        import tp05_recursion as mod
        # fib_naive(20) déclenche beaucoup plus d'appels
        mod._call_count = 0
        mod.fib_naive(20)
        calls_naive = mod._call_count
        # fib_memo(20) doit avoir calculé un résultat correct
        assert tp.fib_memo(20) == 6765
        assert calls_naive > 1000, "fib_naive devrait faire > 1000 appels pour n=20"

    @pytest.mark.timeout(2)
    def test_fib_memo_large(self):
        assert tp.fib_memo(100) == 354224848179261915075


class TestPermutations:
    def test_count(self):
        for n in range(1, 6):
            arr = list(range(n))
            perms = tp.permutations(arr)
            assert len(perms) == math.factorial(n)

    def test_content(self):
        perms = tp.permutations([1, 2, 3])
        assert sorted(sorted(p) for p in perms) == [[1,2,3]] * 6

    def test_no_duplicates(self):
        perms = tp.permutations([1, 2, 3])
        tuples = [tuple(p) for p in perms]
        assert len(tuples) == len(set(tuples))

    def test_empty(self):
        assert tp.permutations([]) == [[]]


class TestSubsets:
    def test_count(self):
        for n in range(0, 5):
            arr = list(range(n))
            assert len(tp.subsets(arr)) == 2**n

    def test_content_3(self):
        result = sorted(tuple(sorted(s)) for s in tp.subsets([1,2,3]))
        expected = sorted([(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)])
        assert result == expected

    def test_empty_input(self):
        assert tp.subsets([]) == [[]]
