"""Tests pytest — TP 16 : Plus Court Chemin"""
import pytest, math
from tp16_plus_court_chemin import dijkstra, bellman_ford, reconstruct_path

INF = math.inf


def build_graph():
    """
    Graphe :
    0 -4- 1 -3- 2
    |     |     |
    2     1     5
    |     |     |
    3 -1- 4 -8- 5
    """
    V = 6
    adj = [[] for _ in range(V)]
    def ae(u, v, w): adj[u].append((v,w)); adj[v].append((u,w))
    ae(0,1,4); ae(0,3,2); ae(1,2,3); ae(1,4,1); ae(3,4,1); ae(2,5,5); ae(4,5,8)
    return adj, V


class TestDijkstra:
    def test_distances(self):
        adj, V = build_graph()
        dist, _ = dijkstra(adj, 0)
        assert dist[0] == 0
        assert dist[3] == 2
        assert dist[4] == 3   # 0→3→4
        assert dist[1] == 4

    def test_prev_allows_path(self):
        adj, V = build_graph()
        dist, prev = dijkstra(adj, 0)
        path = reconstruct_path(prev, 0, 4)
        assert path[0] == 0 and path[-1] == 4
        # Vérifier que c'est bien un chemin valide
        for i in range(len(path)-1):
            neighbors = [v for v,_ in adj[path[i]]]
            assert path[i+1] in neighbors

    def test_unreachable(self):
        # Graphe disconnecté
        adj = [[],[], [(3,1)], [(2,1)]]   # 0,1 isolés
        dist, prev = dijkstra(adj, 0)
        assert dist[2] == INF

    def test_single_node(self):
        dist, _ = dijkstra([[]], 0)
        assert dist[0] == 0


class TestBellmanFord:
    def test_basic(self):
        edges = [(0,1,4),(0,3,2),(1,2,3),(1,4,1),(3,4,1),(2,5,5),(4,5,8)]
        dist = bellman_ford(edges, 6, 0)
        assert dist is not None
        assert dist[4] == 3
        assert dist[3] == 2

    def test_negative_weight(self):
        # 0→1 poids -1
        edges = [(0,1,-1),(1,2,2),(0,2,4)]
        dist = bellman_ford(edges, 3, 0)
        assert dist is not None
        assert dist[2] == 1   # 0→1→2 = -1+2=1

    def test_negative_cycle(self):
        edges = [(0,1,1),(1,2,1),(2,0,-5)]
        assert bellman_ford(edges, 3, 0) is None

    def test_unreachable(self):
        edges = [(0,1,1)]
        dist = bellman_ford(edges, 3, 0)
        assert dist[2] == INF


class TestReconstructPath:
    def test_basic(self):
        adj, V = build_graph()
        _, prev = dijkstra(adj, 0)
        path = reconstruct_path(prev, 0, 5)
        assert path[0] == 0 and path[-1] == 5

    def test_src_equals_dst(self):
        prev = [-1, 0, 1]
        assert reconstruct_path(prev, 0, 0) == [0]

    def test_unreachable(self):
        prev = [-1, -1, -1]
        assert reconstruct_path(prev, 0, 2) == []
