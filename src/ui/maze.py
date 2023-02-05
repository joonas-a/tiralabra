import tkinter

class Maze:
    def __init__(self, master, logic):
        self.master = master
        self.logic = logic

        self.canvas = tkinter.ttk.Frame(self.master, relief="solid", padding=2)
        self.canvas.grid(row=0, column=1)

        self.maze = tkinter.Canvas(
            self.canvas,
            bg="white",
            height=self.logic.get_height(),
            width=self.logic.get_width()
        )
        self.maze.grid(row=0, column=0)

    def update_size(self):
        self.maze.config(
            width=self.logic.get_width(),
            height=self.logic.get_height()
        )
