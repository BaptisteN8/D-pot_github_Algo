"""Tests pytest — TP 15 : Graphes"""
import pytest
from tp15_graphes import Graph


class TestGraph:
    def test_bfs_order(self):
        g = Graph(5)
        g.add_edge(0,1); g.add_edge(0,2); g.add_edge(1,3); g.add_edge(2,4)
        order = g.bfs(0)
        assert order[0] == 0
        assert set(order) == {0,1,2,3,4}
        # BFS : 0 avant 1 et 2, 1 et 2 avant 3 et 4
        assert order.index(0) < order.index(1)
        assert order.index(0) < order.index(2)

    def test_dfs_order(self):
        g = Graph(5)
        g.add_edge(0,1); g.add_edge(0,2); g.add_edge(1,3); g.add_edge(2,4)
        order = g.dfs(0)
        assert order[0] == 0
        assert set(order) == {0,1,2,3,4}

    def test_dfs_recursive(self):
        g = Graph(4)
        g.add_edge(0,1); g.add_edge(1,2); g.add_edge(2,3)
        order = g.dfs_recursive(0)
        assert order[0] == 0 and set(order) == {0,1,2,3}

    def test_is_connected_true(self):
        g = Graph(4)
        g.add_edge(0,1); g.add_edge(1,2); g.add_edge(2,3)
        assert g.is_connected() is True

    def test_is_connected_false(self):
        g = Graph(4)
        g.add_edge(0,1); g.add_edge(2,3)
        assert g.is_connected() is False

    def test_has_cycle_true(self):
        g = Graph(3)
        g.add_edge(0,1); g.add_edge(1,2); g.add_edge(2,0)
        assert g.has_cycle() is True

    def test_has_cycle_false(self):
        g = Graph(4)
        g.add_edge(0,1); g.add_edge(1,2); g.add_edge(2,3)
        assert g.has_cycle() is False

    def test_connected_components(self):
        g = Graph(6)
        g.add_edge(0,1); g.add_edge(2,3); g.add_edge(4,5)
        assert g.connected_components() == 3

    def test_connected_components_one(self):
        g = Graph(5)
        for i in range(4): g.add_edge(i, i+1)
        assert g.connected_components() == 1

    def test_topological_sort(self):
        dag = Graph(4)
        dag.add_directed_edge(0,1); dag.add_directed_edge(0,2)
        dag.add_directed_edge(1,3); dag.add_directed_edge(2,3)
        topo = dag.topological_sort()
        assert len(topo) == 4
        pos = {v: i for i, v in enumerate(topo)}
        assert pos[0] < pos[1] < pos[3]
        assert pos[0] < pos[2] < pos[3]

    def test_topological_sort_linear(self):
        dag = Graph(5)
        for i in range(4): dag.add_directed_edge(i, i+1)
        topo = dag.topological_sort()
        assert topo == [0,1,2,3,4]
