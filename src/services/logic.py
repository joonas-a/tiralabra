#import tkinter

class Logic:
    def __init__(self):
        self.maze = None


    def change_maze_size(self):
        width = int(self.width_input.get())
        height = int(self.height_input.get())
        self.maze.config(
            width=self.cell_size*width,
            height=self.cell_size*height
        )
        print("new width:",self.cell_size*width)
        print("new height:",self.cell_size*height)
