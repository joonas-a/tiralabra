
class Logic:
    def __init__(self, root):
        self.root = root
        self.cell_size = 20
        self.width = 20
        self.height = 20
        self.maze_layout = None

        self.generate_empty_maze()

    def get_width(self):
        return self.cell_size * self.width

    def get_height(self):
        return self.cell_size * self.height

    def generate_empty_maze(self):
        self.maze_layout = [
            [0 for i in range(self.width)] for i in range(self.height)]

    def change_maze_size(self, new_width, new_height, maze):
        self.width = int(new_width)
        self.height = int(new_height)
        self.generate_empty_maze()
        maze.update_size()
