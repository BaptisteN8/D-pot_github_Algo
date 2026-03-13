# TP 04 — Listes Doublement Chaînées

## Exercice 1 — Classe DoublyLinkedList (10 pts)
Implémentez avec gestion correcte de `head` et `tail` :
- `push_front(val)` / `push_back(val)` — **O(1)**
- `pop_front()` / `pop_back()` — **O(1)**
- `insert_after(node, val)` / `remove(node)` — **O(1)**
- `find(val)` — **O(n)** ; `__len__` / `__iter__`

## Exercice 2 — Inversion (4 pts)
- `reverse_iterative(lst)` — O(n) temps, O(1) espace
- `reverse_recursive(node)` — O(n) temps, O(n) pile

## Exercice 3 — Algorithme de Floyd (3 pts)
Sur une liste simplement chaînée `SNode` :
`has_cycle(head)` — O(n) temps, O(1) espace.

## Exercice 4 — K-ième depuis la fin (3 pts)
`kth_from_end(head, k)` — un seul parcours, deux pointeurs.
