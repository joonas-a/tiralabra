import random


class Kruskals:
    def __init__(self, layout, maze, visualize):
        self.grid = layout
        self.maze = maze
        self.visualize = visualize
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.sets = DisjointSet()
        self.walls = []
        self.populate_walls()

    def populate_walls(self):
        for row_count, row in enumerate(self.grid):
            for col_count, cell in enumerate(row):
                if cell == 1 and not (row_count % 2 == 1 and col_count % 2 == 1):
                    self.add_wall(col_count, row_count)
        random.shuffle(self.walls)

    def add_wall(self, col, row):
        if col == 0 or col == (self.width - 1) or col % 2 == 0:
            self.walls.append((col, row, "vertical"))
        elif row == 0 or row == (self.height - 1) or row % 2 == 0:
            self.walls.append((col, row, "horizontal"))
        else:
            # print("something went wrong adding walls to the list")
            pass

    def run(self):
        while self.walls:
            col, row, dir = self.walls.pop()

            if dir == "horizontal":
                col_a = col - 1
                col_b = col + 1
                row_a, row_b = row, row
            elif dir == "vertical":
                row_a = row - 1
                row_b = row + 1
                col_a, col_b = col, col
            else:
                # print("failed with", row, col)
                continue

            set1 = self.sets.find((row_a, col_a))
            set2 = self.sets.find((row_b, col_b))
            if set1 != set2:
                self.sets.union(set1, set2)
                self.grid[row][col] = 0
                self.grid[row_a][col_a] = 0
                self.grid[row_b][col_b] = 0
                if self.visualize:
                    self.maze.maze.after(30, self.maze.draw_passage(row, col))
                    self.maze.draw_passage(row_a, col_a)
                    self.maze.draw_passage(row_b, col_b)
                    self.maze.maze.update()

        return self.grid


class DisjointSet:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    def find(self, value):
        if value not in self.parents:
            self.parents[value] = value
            self.ranks[value] = 0
            return value
        if self.parents[value] != value:
            self.parents[value] = self.find(self.parents[value])
        return self.parents[value]

    def union(self, set1, set2):
        rootx = self.find(set1)
        rooty = self.find(set2)
        if rootx != rooty:
            if self.ranks[rootx] < self.ranks[rooty]:
                self.parents[rootx] = rooty
            else:
                self.parents[rooty] = rootx
                if self.ranks[rootx] == self.ranks[rooty]:
                    self.ranks[rootx] += 1


# driver code for testing disjoint sets data structure
if __name__ == "__main__":
    D = DisjointSet()
    print(D.parents)
    print(D.find(1))
    D.union(1, 2)
    print(D.find(1))
    print(D.find(2))
    D.union(2, 4)
    print(D.find(2))
    print(D.find(3))
    print(D.parents)
