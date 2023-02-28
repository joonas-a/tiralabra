import sys
import unittest
from unittest.mock import MagicMock
from services.logic import Logic

sys.path.append("..")


class TestMazeGeneration(unittest.TestCase):

    def setUp(self):
        self.logic = Logic()
        self.mock_maze = MagicMock()
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
        self.find = any(2 in row for row in self.logic.maze_layout)
        self.assertEqual(self.find, True)
        self.logic.kruskals(self.mock_maze)
        self.find = any(2 in row for row in self.logic.maze_layout)
        self.assertEqual(self.find, False)

    def test_maze_dimension_change(self):
        width = 50
        height = 23
        new_width = (width * 2 - 1) * self.logic.cell_size
        new_height = (height * 2 - 1) * self.logic.cell_size
        self.logic.change_maze_size(width, height, self.mock_maze)
        self.assertEqual(self.logic.get_height(), new_height)
        self.assertEqual(self.logic.get_width(), new_width)
