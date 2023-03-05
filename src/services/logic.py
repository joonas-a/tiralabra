import time
from .kruskal import Kruskals
from . backtracker import Backtracker


class Logic:
    """The main logic component for storing the state of the application

    Is initialized upon the start of the application. Takes no args, but the
    properties can be later altered through helper methods and algorithms.
    """

    def __init__(self):
        self.cell_size = 10
        self.width = 41
        self.height = 41
        self.maze_layout = None
        self.runtime = 0

        self.generate_empty_maze()

    def get_width(self):
        return self.cell_size * self.width

    def get_height(self):
        return self.cell_size * self.height

    def generate_empty_maze(self):
        # Generates the matrix for displaying the maze
        # 0 for path, 1 for solid wall, 2 for unvisited cell
        # 1 & 2 are by default drawn black in the maze
        self.maze_layout = [
            [1 if i % 2 == 1 or j % 2 == 1 else 2 for j in range(self.width)] for i in range(self.height)]

    def change_maze_size(self, new_width, new_height, maze):
        self.width = int(new_width) + int(new_width) - 1
        self.height = int(new_height) + int(new_height) - 1
        self.generate_empty_maze()
        maze.update_size()

    def kruskals(self, maze, visualize=False):
        self.runtime = 0
        start = time.time()
        self.generate_empty_maze()
        maze.draw_maze(self.maze_layout)
        kruskals = Kruskals(self.maze_layout, maze, visualize)
        self.maze_layout = kruskals.run()
        maze.draw_maze(self.maze_layout)
        end = time.time()
        self.runtime = end - start

    def backtracker(self, maze, visualize=False):
        self.runtime = 0
        start = time.time()
        self.generate_empty_maze()
        maze.draw_maze(self.maze_layout)
        backtracker = Backtracker(self.maze_layout, maze, visualize)
        self.maze_layout = backtracker.run()
        maze.draw_maze(self.maze_layout)
        end = time.time()
        self.runtime = end - start
