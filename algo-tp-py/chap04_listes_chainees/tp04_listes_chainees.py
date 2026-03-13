"""
TP 04 — Listes Doublement Chaînées
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Liste doublement chaînée avec head, tail et taille."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, val) -> None:
        """Insertion en tête — O(1)."""
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def push_back(self, val) -> None:
        """Insertion en queue — O(1)."""
        new_node = Node(val)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def pop_front(self):
        """
        Suppression et retour de la valeur en tête — O(1).
        Lève IndexError si vide.
        """
        if self.head is None:
            raise IndexError("pop from empty list")
        val = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return val

    def pop_back(self):
        """
        Suppression et retour de la valeur en queue — O(1).
        Lève IndexError si vide.
        """
        if self.tail is None:
            raise IndexError("pop from empty list")
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return val

    def insert_after(self, node: Node, val) -> Node:
        """
        Insère val après node, retourne le nouveau nœud — O(1).
        """
        new_node = Node(val)
        new_node.next = node.next
        new_node.prev = node
        if node.next:
            node.next.prev = new_node
        else:
            self.tail = new_node
        node.next = new_node
        self._size += 1
        return new_node

    def remove(self, node: Node) -> None:
        """Supprime node de la liste — O(1)."""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self._size -= 1

    def find(self, val) -> Node | None:
        """Retourne le premier nœud avec data==val, ou None — O(n)."""
        cur = self.head
        while cur:
            if cur.data == val:
                return cur
            cur = cur.next
        return None

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        """Parcours de head vers tail."""
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def to_list(self) -> list:
        return list(self)


# ── Exercice 2 ────────────────────────────────────────────────────────────────

def reverse_iterative(lst: DoublyLinkedList) -> None:
    """
    Inverse la liste en place — O(n) temps, O(1) espace.
    Pour chaque nœud, échange prev et next, puis swap head et tail.
    """
    cur = lst.head
    while cur:
        cur.prev, cur.next = cur.next, cur.prev
        cur = cur.prev  # après échange, prev est l'ancien next
    lst.head, lst.tail = lst.tail, lst.head


# ── Exercice 3 — Algorithme de Floyd ─────────────────────────────────────────

class SNode:
    """Nœud de liste simplement chaînée pour l'exercice Floyd."""
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(head: SNode | None) -> bool:
    """
    Détecte un cycle dans une liste simplement chaînée.
    Algorithme du lièvre et de la tortue — O(n) temps, O(1) espace.
    TODO : slow avance de 1, fast avance de 2
    """
    if not head:
        return False
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# ── Exercice 4 ────────────────────────────────────────────────────────────────

def kth_from_end(head: SNode | None, k: int) -> int:
    """
    Retourne la valeur du k-ième élément depuis la fin (k=1 = dernier).
    Un seul parcours, deux pointeurs distants de k.
    Lève ValueError si k > longueur.
    """
    if not head or k <= 0:
        raise ValueError("Invalid k or empty list")
    first = second = head
    for _ in range(k - 1):
        if not first.next:
            raise ValueError("k is larger than list length")
        first = first.next
    while first.next:
        first = first.next
        second = second.next
    return second.val