from services.logic import Logic


class PerformanceTester:
    """ A separate program for running performance tests on the algorithms without visualization
        Simple CLI which asks for parameters before returning the results

        Contains no input validation/limitations; simulating with large parameters will take
        a _very_ long time.
    """

    def __init__(self):
        self.logic = Logic()
        self.logic.max_height = 999999999999999
        self.logic.max_width = 999999999999999
        self.maze = MazeMock()

    def main_loop(self):
        while True:
            print("Please select the size of the maze")
            height = input("Height: ")
            width = input("Width: ")
            self.logic.change_maze_size(width, height, self.maze)

            simulations = input("How many iterations? ")

            print(
                f"Simulating maze generation on a {height} * {width} maze {simulations} times...")
            self.simulate(simulations)

            if input("New simulation? y/n: ").lower() == "n":
                break

    def simulate(self, number):
        """Run simulations on both algorithms 'number' times
           Collects runtimes to a list for comparison later
        """
        kruskal_runtimes = []
        backtracker_runtimes = []

        # Simulate kruskals
        for _ in range(int(number)):
            self.logic.kruskals(self.maze, False)
            kruskal_runtimes.append(self.logic.runtime)

        # Simulate backtracker
        for _ in range(int(number)):
            self.logic.backtracker(self.maze, False)
            backtracker_runtimes.append(self.logic.runtime)

        self.show_results(kruskal_runtimes, backtracker_runtimes)

    def show_results(self, kruskal, backtracker):
        avg_kruskal = sum(kruskal) / len(kruskal)
        avg_backtracker = sum(backtracker) / len(backtracker)
        difference = abs(avg_kruskal-avg_backtracker)
        percentage = difference / ((avg_kruskal + avg_backtracker) / 2) * 100
        faster = None
        if avg_kruskal < avg_backtracker:
            faster = "kruskals algorithm"
        else:
            faster = "backtracker"

        print()
        print(f"{'Avg runtime for kruskals algorithm:' : <40} {avg_kruskal:.5f} s")
        print(f"{'Avg runtime for backtracker:' : <40} {avg_backtracker:.5f} s")
        print(
            f"On average the {faster} was faster by {difference:.5f} s or {percentage:.2f} %")
        print()


class MazeMock:
    def __init__(self):
        pass

    def update_size(self, *args):
        pass

    def draw_maze(self, *args):
        pass


if __name__ == "__main__":
    app = PerformanceTester()
    app.main_loop()
