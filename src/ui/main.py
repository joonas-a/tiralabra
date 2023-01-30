import tkinter
from tkinter import ttk as tk


root = tkinter.Tk()
root.title("Maze Generator")
root.resizable(width=False, height=False)

# contains all other frames
content = tk.Frame(root)
content.grid(column=0, row=0)

navigation = tk.Frame(content, padding=2)
canvas = tk.Frame(content, relief="solid", padding=2)

navigation.grid(column=0, row=0, sticky="n")
canvas.grid(column=1, row=0)

title_tabel = tk.Label(navigation, text="Maze Generator", font=("Arial", 14))
title_tabel.grid(row=0, column=0, columnspan=2, pady=5, padx=4)

size_label = tk.Label(navigation, text="Maze size (cells)", font=("Arial", 11))
size_label.grid(row=2, column=0, columnspan=2, sticky="W", padx=4)

height_label = tk.Label(navigation, text="Height")
width_label = tk.Label(navigation, text="Width")
height_label.grid(row=3, column=0, pady=3, padx=4, sticky="W")
width_label.grid(row=4, column=0, pady=3, padx=4, sticky="W")

# input needs to be validated for integer only
height_input = tk.Entry(navigation, width=7)
width_input = tk.Entry(navigation, width=7)
height_input.grid(row=3, column=0, pady=3, sticky="E")
width_input.grid(row=4, column=0, pady=3, sticky="E")

set_size = tk.Button(navigation, text="Set")
set_size.grid(row=5, column=0)

algo1 = tk.Button(navigation, text="Algorithm 1")
algo1.grid(row=6, column=0, pady=5)

algo2 = tk.Button(navigation, text="Algorithm 2")
algo2.grid(row=7, column=0, pady=5)

button = tk.Checkbutton(navigation, text="Visualize")
button.grid(row=8, column=0)

maze = tkinter.Canvas(canvas)
maze.grid(row=0, column=0)

root.mainloop()
