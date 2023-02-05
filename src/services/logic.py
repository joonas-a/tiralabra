
class Logic:
    def __init__(self, root):
        self.root = root
        self.cell_size = 20
        self.width = 20
        self.height = 20

    def get_width(self):
        return self.cell_size * self.width

    def get_height(self):
        return self.cell_size * self.height

    def change_maze_size(self, new_width, new_height, maze):
        self.width = int(new_width)
        self.height = int(new_height)
        maze.update_size()

        print("new width:", self.get_width())
        print("new height:", self.get_height())
