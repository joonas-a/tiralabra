import sys
import unittest
from unittest.mock import MagicMock
from services.logic import Logic

sys.path.append("..")


class TestMazeGeneration(unittest.TestCase):

    def setUp(self):
        self.logic = Logic()
        self.logic.generate_empty_maze()

    def test_empty_maze_is_generated(self):
        layout = self.logic.maze_layout
        self.find = any(2 in row for row in layout)
        self.assertEqual(self.find, True)
        self.find = any(1 in row for row in layout)
        self.assertEqual(self.find, True)
        self.find = any(0 in row for row in layout)
        self.assertEqual(self.find, False)

    def test_no_unvisited_cells_after_kruskal(self):
        mock_maze = MagicMock()
        self.find = any(2 in row for row in self.logic.maze_layout)
        self.assertEqual(self.find, True)
        self.logic.kruskals(mock_maze)
        self.find = any(2 in row for row in self.logic.maze_layout)
        self.assertEqual(self.find, False)
