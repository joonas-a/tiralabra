import tkinter


class Maze:
    def __init__(self, master, logic):
        self.master = master
        self.logic = logic

        self.canvas_frame = tkinter.ttk.Frame(
            self.master, relief="solid", padding=5)
        self.canvas_frame.grid(row=0, column=1)

        self.maze = tkinter.Canvas(
            self.canvas_frame,
            bg="white",
            height=self.logic.get_height(),
            width=self.logic.get_width()
        )
        self.maze.grid(row=0, column=0)
        self.draw_maze(self.logic.maze_layout)

    def draw_maze(self, layout):
        for column_count, row in enumerate(layout):
            for row_count, cell in enumerate(row):
                cell_color = "black" if cell == 1 else "white"
                self.maze.create_rectangle(
                    self.logic.cell_size*row_count,
                    self.logic.cell_size*column_count,
                    self.logic.cell_size*(row_count+1),
                    self.logic.cell_size*(column_count+1),
                    outline="grey",
                    fill=cell_color
                )

    def update_size(self):
        self.maze.config(
            width=self.logic.get_width(),
            height=self.logic.get_height()
        )
        self.draw_maze(self.logic.maze_layout)
