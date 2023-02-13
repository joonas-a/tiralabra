import tkinter


class Maze:
    """Responsible for representing maze on the right side of the application

    Creates a new frame for the canvas displaying the maze. Provides functions
    for drawing the maze for given layout, or individual cells one at a time.

    Args:
        master: frame which stores the newly created canvas frame, useful for
            easier customization of the UI
        logic: logic component of the application, stores the state
            of the maze
    """

    def __init__(self, master, logic):
        self.master = master
        self.logic = logic
        self.layout = self.logic.maze_layout

        self.canvas_frame = tkinter.Frame(
            self.master, relief="groove", bg="grey")
        self.canvas_frame.grid(row=0, column=1)

        self.maze = tkinter.Canvas(
            self.canvas_frame,
            bg='black',
            height=self.logic.get_height(),
            width=self.logic.get_width()
        )
        self.maze.grid(row=0, column=0, padx=5, pady=5)
        self.draw_maze(self.logic.maze_layout)

    def draw_maze(self, layout):
        """Accepts a matrix, in which 0s are drawn as path"""
        for column_count, row in enumerate(layout):
            for row_count, cell in enumerate(row):
                cell_color = "white" if cell == 0 else "black"
                self.maze.create_rectangle(
                    self.logic.cell_size*row_count+2,
                    self.logic.cell_size*column_count+2,
                    self.logic.cell_size*(row_count+1)+2,
                    self.logic.cell_size*(column_count+1)+2,
                    outline="",
                    fill=cell_color
                )

    def draw_passage(self, x, y):
        self.maze.create_rectangle(
            self.logic.cell_size*y+2,
            self.logic.cell_size*x+2,
            self.logic.cell_size*(y+1)+2,
            self.logic.cell_size*(x+1)+2,
            outline="",
            fill="white"
        )

    def update_size(self):
        self.maze.config(
            width=self.logic.get_width(),
            height=self.logic.get_height()
        )
        self.draw_maze(self.logic.maze_layout)
