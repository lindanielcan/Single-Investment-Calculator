from tkinter import Tk
from tkinter import Toplevel
from view import main_screen

class ResultScreen():
    def __init__(self, Tk):
        self.main_screen = Tk
        pass

    def open(self):
        top = Toplevel(self.main_screen, height=500, width=600, bg=main_screen.BACKGROUND_COLOR)
        top.mainloop()
