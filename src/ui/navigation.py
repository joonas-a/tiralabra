from tkinter import ttk as tk


class Navigation:
    def __init__(self, master, logic, maze):
        self.master = master
        self.logic = logic
        self.maze = maze
        self.navigation = tk.Frame(self.master, padding=2)
        self.navigation.grid(column=0, row=0, sticky="n")

        title_tabel = tk.Label(
            self.navigation, text="Maze Generator", font=("Arial", 14))
        size_label = tk.Label(
            self.navigation, text="Maze size (cells)", font=("Arial", 11))
        height_label = tk.Label(self.navigation, text="Height")
        width_label = tk.Label(self.navigation, text="Width")
        self.height_input = tk.Entry(self.navigation, width=7)
        self.width_input = tk.Entry(self.navigation, width=7)
        set_size = tk.Button(
            self.navigation,
            text="Set",
            command=self.set_size
        )
        algo1 = tk.Button(self.navigation, text="Algorithm 1")
        algo2 = tk.Button(self.navigation, text="Algorithm 2",)
        visualize_button = tk.Checkbutton(self.navigation, text="Visualize")

        title_tabel.grid(row=0, column=0, columnspan=2, pady=5, padx=4)
        size_label.grid(row=2, column=0, columnspan=2, sticky="W", padx=4)
        # input needs to be validated for integer only
        height_label.grid(row=3, column=0, pady=3, padx=4, sticky="W")
        self.height_input.grid(row=3, column=0, pady=3, sticky="E")
        width_label.grid(row=4, column=0, pady=3, padx=4, sticky="W")
        self.width_input.grid(row=4, column=0, pady=3, sticky="E")
        set_size.grid(row=5, column=0)
        algo1.grid(row=6, column=0, pady=5)
        algo2.grid(row=7, column=0, pady=5)
        visualize_button.grid(row=8, column=0)

    def set_size(self):
        width = self.width_input.get()
        height = self.height_input.get()
        self.logic.change_maze_size(width, height, self.maze)
