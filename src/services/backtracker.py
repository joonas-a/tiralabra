from random import choice


class Backtracker:
    def __init__(self, layout, maze, visualize, sleep_timer):
        self.grid = layout
        self.maze = maze
        self.visualize = visualize
        self.sleep = sleep_timer
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.visited = set()
        self.stack = []

    def run(self):
        self.stack.append((0, 0))
        while self.stack:
            current_cell = self.stack.pop()
            next_cell = self.find_options(current_cell)

            if self.options:
                self.stack.append(current_cell)
                # remove the wall between the current cell and the chosen cell
                self.grid[current_cell[1]][current_cell[0]] = 0
                self.grid[next_cell[1][1]][next_cell[1][0]] = 0
                self.grid[next_cell[0][1]][next_cell[0][0]] = 0

                if self.visualize:
                    self.maze.maze.after(self.sleep, self.maze.draw_passage(
                        current_cell[1], current_cell[0]))
                    self.maze.draw_passage(next_cell[1][1], next_cell[1][0])
                    self.maze.draw_passage(next_cell[0][1], next_cell[0][0])
                    self.maze.maze.update()

                self.visited.add(next_cell[0])
                self.stack.append(next_cell[0])

            self.visited.add(current_cell)
        return self.grid

    def find_options(self, current_cell):
        """ Initializes/flushes the options list, and finds any possible
            moves for current cell

            Returns a tuple of tuples, where first is the new cell, and second
            is the wall in between
        """
        self.options = []
        Y = current_cell[0]
        X = current_cell[1]

        if current_cell[0] >= 2 and (Y - 2, X) not in self.visited:
            self.options.append(((Y - 2, X), (Y - 1, X)))
        if current_cell[0] < self.width - 2 and (Y + 2, X) not in self.visited:
            self.options.append(((Y + 2, X), (Y + 1, X)))
        if current_cell[1] >= 2 and (Y, X - 2) not in self.visited:
            self.options.append(((Y, X - 2), (Y, X - 1)))
        if current_cell[1] < self.height - 2 and (Y, X + 2) not in self.visited:
            self.options.append(((Y, X + 2), (Y, X + 1)))

        if self.options:
            # print("")
            #print("current moves:")
            # print(self.options)
            return choice(self.options)
        return None
