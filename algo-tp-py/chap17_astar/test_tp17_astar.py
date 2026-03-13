"""Tests pytest — TP 17 : A* et Recherche Informée"""
import pytest, math
from tp17_astar import (
    manhattan, chebyshev, euclidean,
    astar, astar_with_count, bfs_on_grid, bfs_with_count,
)


MAZE = [
    "...........",
    ".#########.",
    "...........",
    ".#########.",
    "...........",
]
START = (0, 0)
END   = (4, 10)

BLOCKED = [
    "..#..",
    "..#..",
    "..#..",
    "..#..",
    "..#..",
]


class TestHeuristics:
    def test_manhattan(self):
        assert manhattan((0,0), (3,4)) == 7
        assert manhattan((0,0), (0,0)) == 0
        assert manhattan((2,3), (5,1)) == 5

    def test_chebyshev(self):
        assert chebyshev((0,0), (3,4)) == 4
        assert chebyshev((0,0), (0,0)) == 0

    def test_euclidean(self):
        assert abs(euclidean((0,0), (3,4)) - 5.0) < 1e-9
        assert euclidean((0,0), (0,0)) == 0.0


class TestAstar:
    def test_finds_path(self):
        path = astar(MAZE, START, END)
        assert path, "A* devrait trouver un chemin"
        assert path[0] == START
        assert path[-1] == END

    def test_path_valid(self):
        path = astar(MAZE, START, END)
        for r, c in path:
            assert MAZE[r][c] != '#', f"Cellule mur ({r},{c}) dans le chemin"

    def test_path_connected(self):
        path = astar(MAZE, START, END)
        for i in range(len(path)-1):
            r1,c1 = path[i]; r2,c2 = path[i+1]
            assert abs(r1-r2) + abs(c1-c2) == 1, "Pas de saut dans le chemin"

    def test_no_path(self):
        path = astar(BLOCKED, (0,0), (0,4))
        assert path == []

    def test_start_equals_end(self):
        path = astar(MAZE, START, START)
        assert path == [START]

    def test_optimal_simple(self):
        grid = [".....", ".....", "....."]
        start, end = (0,0), (2,4)
        path = astar(grid, start, end)
        assert len(path) - 1 == 6   # Manhattan = 6 = chemin optimal

    @pytest.mark.parametrize("h", [manhattan, chebyshev, euclidean])
    def test_with_different_heuristics(self, h):
        path = astar(MAZE, START, END, h=h)
        assert path and path[0] == START and path[-1] == END

    def test_optimal_length_matches_bfs(self):
        """A* doit retourner un chemin de même longueur que BFS (optimal)."""
        path_astar = astar(MAZE, START, END)
        path_bfs   = bfs_on_grid(MAZE, START, END)
        assert len(path_astar) == len(path_bfs)


class TestAstarVsBFS:
    def test_astar_explores_less(self):
        """A* devrait explorer moins de cellules que BFS sur ce labyrinthe."""
        _, astar_cnt = astar_with_count(MAZE, START, END)
        _, bfs_cnt   = bfs_with_count(MAZE, START, END)
        assert astar_cnt <= bfs_cnt, (
            f"A* ({astar_cnt}) devrait explorer <= cellules que BFS ({bfs_cnt})"
        )

    def test_bfs_optimal(self):
        path = bfs_on_grid(MAZE, START, END)
        assert path and path[0] == START and path[-1] == END
