from .kruskal import Kruskals


class Logic:
    def __init__(self, root):
        self.root = root
        self.cell_size = 10
        self.width = 41
        self.height = 41
        self.maze_layout = None

        self.generate_empty_maze()

    def get_width(self):
        return self.cell_size * self.width

    def get_height(self):
        return self.cell_size * self.height

    def generate_empty_maze(self):
        # 1 for wall, 2 for unvisited cell
        self.maze_layout = [
            [1 if i % 2 == 1 or j % 2 == 1 else 2 for j in range(self.width)] for i in range(self.height)]

    def change_maze_size(self, new_width, new_height, maze):
        self.width = int(new_width) + int(new_width) - 1
        self.height = int(new_height) + int(new_height) - 1
        self.generate_empty_maze()
        maze.update_size()

    def kruskals(self, maze, visualize=False):
        self.generate_empty_maze()
        maze.draw_maze(self.maze_layout)
        kruskals = Kruskals(self.maze_layout, maze, visualize)
        self.maze_layout = kruskals.run()
        maze.draw_maze(self.maze_layout)
