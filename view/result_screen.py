from tkinter import Tk
from tkinter import Toplevel
from view import main_screen
from controller import result_screen_controller


class ResultScreen():
    def __init__(self, Tk):
        self.main_screen = Tk
        self.result_screen_controller = result_screen_controller.ResultScreenController()
        self.data = []

    def open(self):
        top = Toplevel(self.main_screen, height=500, width=600, bg=main_screen.BACKGROUND_COLOR, highlightthickness=0)
        top.resizable(False, False)
        top.title("Result")

        # Apply result methods here.

        



        # ---

        top.mainloop()

    def get_investment_data(self, data):
        """Gets user inputs from the main screen."""
        self.data = data

