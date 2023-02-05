import tkinter
from tkinter import ttk as tk
from navigation import Navigation
#from ..services.logic import Logic

class MainLoop(tkinter.Tk()):

    def __init__(self, root):
        self.root = root
        self.title = "Maze Generator"
        self.cell_size = 20
        self.maze = None
        self.navigation = None
        #self.logic = Logic

        self.initialize()

    def initialize(self):
        root = self.root
        root.title(self.title)
        root.resizable(width=False, height=False)

        # contains all other frames
        content = tk.Frame(root)
        content.grid(column=0, row=0)

        self.navigation = Navigation(content)
        #navigation = tk.Frame(content, padding=2)
        canvas = tk.Frame(content, relief="solid", padding=2)

        #navigation.grid(column=0, row=0, sticky="n")
        canvas.grid(column=1, row=0)

        self.maze = tkinter.Canvas(canvas, bg="white", height=20*self.cell_size, width=20*self.cell_size)
        self.maze.grid(row=0, column=0)

    # logic needs to be separated from the ui

    def run(self):
        self.root.mainloop()


app = MainLoop()
app.run()
