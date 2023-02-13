import tkinter
from ui.main import MainLoop
from services.logic import Logic


class App:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Maze Generator")
        self.root.resizable(width=False, height=False)
        self.logic = Logic()
        self.loop = MainLoop(self.root, self.logic)

    def run(self):
        self.loop.run()


if __name__ == "__main__":
    app = App()
    app.run()
