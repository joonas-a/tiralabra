import sys
import unittest
from unittest.mock import MagicMock
from services.logic import Logic

sys.path.append("..")

''' Work in progress

class TestMazeIsPerfect(unittest.TestCase):
    """
    A perfect maze means a maze which only has one path from one point to another,
    meaning no loops/cycles and no unreachable areas.

    To test for those a DFS-search is conducted through the maze
    """


    def setUp(self):
        self.logic = Logic()
        self.maze = MagicMock()
        # print(self.logic.maze_layout)

    def test_for_cycles_in_maze(self):
        self.logic.kruskals(self.maze)
        matrix = self.logic.maze_layout
        #cycles = Cycles(matrix)
        visited = set()
        self.dfs(visited, matrix, (0, 0))

    def dfs(self, visited, graph, node: tuple):
        node_val = self.matrix[node[0]][node[1]]
        if node not in visited and node_val == 0:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                self.dfs(visited, graph, neighbour)

'''
