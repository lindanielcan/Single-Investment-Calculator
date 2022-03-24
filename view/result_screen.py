from tkinter import Toplevel, Label
from view import main_screen
from controller import result_screen_controller


class ResultScreen:
    def __init__(self, Tk):
        self.main_screen = Tk
        self.result_screen_controller = result_screen_controller.ResultScreenController()
        self.data = []
        self.calculated_data = {}

        # Storing entry box information in a list.
        self.label_info = [
            {"key": "yearly_average_growth", "row": 0, "column": 0},
            {"key": "yearly_average_growth_with_dividend", "row": 1, "column": 0},
            {"key": "expense_fee_paid", "row": 2, "column": 0},
            {"key": "total_dividend_received", "row": 3, "column": 0},
            {"key": "total_investment_return", "row": 4, "column": 0}
        ]

    def open(self):
        top = Toplevel(self.main_screen, highlightthickness=0)

        top.resizable(False, False)
        top.config(bg=main_screen.BACKGROUND_COLOR)
        top.title("Result")
        # Apply result methods here.

        # Send user inputs to result screen controller.
        self.result_screen_controller.get_investment_data(self.data)

        # Receive calculated data from the result screen controller.
        self.calculated_data = self.result_screen_controller.get_calculated_data()

        # Creates labels to display calculated data.
        for label in self.label_info:
            self.show_label(top, self.calculated_data[label["key"]], label['row'], label['column'])
        # ---

        top.mainloop()

    def set_investment_data(self, data):
        """Sets user inputs from the main screen."""
        self.data = data

    def show_label(self, screen, text, row, col, columnspan=1):
        """
        Creates a label and display it on the screen
        :param screen: Tk screen - screen
        :param row: label row index
        :param col: label row index
        """
        Label(screen, text=text, bg=main_screen.BACKGROUND_COLOR,
              font=('Arial', 10, 'bold',)).grid(row=row, column=col, columnspan=columnspan)
