from tkinter import Tk
from tkinter import Toplevel


class ResultScreen():
    def __init__(self, Tk):
        self.main_screen = Tk
        pass

    def open(self):
        top = Toplevel(self.main_screen)
        top.mainloop()
