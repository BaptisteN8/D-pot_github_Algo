# 🎓 Algorithmique Avancée — Travaux Pratiques (Python)

> **3ème année — Génie Informatique**
> Structures de données · Algorithmes · Complexité — 17 TPs

---

## 📁 Structure du dépôt

```
algo-tp/
├── README.md
├── requirements.txt          ← pytest + pytest-timeout
├── chap01_introduction/
│   ├── SUJET.md              ← Énoncé complet
│   ├── tp01.py               ← Code à compléter (TODO)
│   └── test_tp01.py          ← Tests pytest (NE PAS MODIFIER)
├── chap02_tableaux/
│   └── ...
└── ... (17 chapitres)
```

---

## 📚 Programme

| # | Chapitre | Thème du TP | Durée |
|---|----------|-------------|-------|
| 01 | Introduction | Complexité empirique & Big-O | 1h |
| 02 | Tableaux | Rotations, recherche binaire, Kadane | 1h |
| 03 | Tris simples | Bubble, Selection, Insertion | 1h30 |
| 04 | Listes chaînées | Liste doublement chaînée complète | 1h30 |
| 05 | Récursion | Classiques récursifs + mémoïsation | 1h |
| 06 | Diviser pour régner | Tri fusion, tri rapide, quickselect | 1h30 |
| 07 | Tris linéaires | Counting, Radix, Bucket sort | 1h |
| 08 | Piles | Implémentation + RPN + MinStack | 1h |
| 09 | Files | File circulaire + BFS + simulateur | 1h |
| 10 | Tables de hachage | Annuaire haché + adressage ouvert | 1h30 |
| 11 | BST | Arbre binaire de recherche complet | 1h30 |
| 12 | Arbres AVL | Rotations et équilibrage | 2h |
| 13 | Arbres Rouge-Noir | Vérificateur de propriétés RBT | 1h30 |
| 14 | Tas binaires | MinHeap + HeapSort + K plus grands | 1h |
| 15 | Graphes | BFS, DFS, composantes, tri topologique | 1h30 |
| 16 | Plus court chemin | Dijkstra + Bellman-Ford | 1h30 |
| 17 | Recherche informée | A* sur labyrinthe 2D + heuristiques | 2h |

---

## 🚀 Démarrage rapide

### Prérequis
```bash
python --version   # >= 3.9
pip install -r requirements.txt
```

### Lancer les tests d'un TP
```bash
# Depuis la racine du dépôt
pytest chap03_tris_simples/ -v

# Avec affichage détaillé + timeout
pytest chap03_tris_simples/ -v --timeout=5

# Tous les TPs d'un coup
pytest -v --timeout=5
```

### Workflow recommandé
1. Lire `SUJET.md`
2. Ouvrir `tp_XX.py`, compléter les `# TODO`
3. Lancer `pytest` — les tests verts = exercices réussis
4. Valider toutes les étoiles ⭐ avant de rendre

---

## 📐 Notation (sur 20 pts par TP)

| Critère | Points |
|---------|--------|
| Tests pytest qui passent | 10 |
| Complexité correcte (commentée) | 4 |
| Qualité du code (lisibilité, docstrings) | 3 |
| Cas limites gérés | 3 |

---

## 🔧 Convention des fichiers

Chaque `tp_XX.py` contient :
- Les **classes/fonctions** à implémenter
- Des **`# TODO`** précisant la complexité attendue
- Des docstrings indiquant le comportement

```python
def merge_sort(arr: list) -> list:
    """
    Trie arr par ordre croissant (tri fusion stable).
    Complexité attendue : O(n log n) temps, O(n) espace.
    # TODO: implémenter
    """
    raise NotImplementedError
```

Les fichiers `test_tp_XX.py` utilisent **pytest** — ne pas les modifier.

---

*Ressources : cours PDF sur Moodle · https://visualgo.net · https://docs.python.org*
