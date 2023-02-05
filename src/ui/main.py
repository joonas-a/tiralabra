from tkinter import ttk as tk
from ui.navigation import Navigation
from ui.maze import Maze


class MainLoop:

    def __init__(self, root, logic):
        self.root = root
        self.logic = logic
        self.root.title = "Maze Generator"
        self.root.resizable(width=False, height=False)
        self.maze = None
        self.navigation = None

        self.initialize()

    def initialize(self):
        # helper frame to contain all other frames
        content = tk.Frame(self.root)
        content.grid(column=0, row=0)

        self.maze = Maze(content, self.logic)
        self.navigation = Navigation(content, self.logic, self.maze)

    def run(self):
        self.root.mainloop()
