import tkinter
from tkinter import ttk
import os, sys
import datetime

script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")

from controller import main_screen_controller

BACKGROUND_COLOR = 'white'


class MainScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.controller = main_screen_controller.MainScreenController()
        self.geometry('1500x800')
        self.years_before_now = [datetime.datetime.now().year - year for year in range(0, 41)]
        self.dividend_frequency = ['monthly', 'Quarterly', 'yearly']
        self.investing_frequency = ['weekly', 'monthly', 'Quarterly', 'yearly']
        self.investment_data = []
        self.years_before_now.reverse()

        # Set the screen to not resizable.
        self.resizable(False, False)

        # Row 1 content
        self.show_label("Investing Title:", 0, 0)
        self.show_entry_box(0, 1)

        # Row 2
        self.message = "Please enter the following information for the investment"
        self.show_label(self.message, 1, 0, 5)

        # Row 3
        self.show_label("Start Year:", 2, 0)
        self.show_combobox(2, 1, self.years_before_now)

        self.show_label("Start year Price:", 2, 2)
        self.show_entry_box(2, 3)

        self.show_label("Current Price:", 2, 4)
        self.show_entry_box(2, 5)

        # Row 4
        self.show_label("Dividend Yield:", 3, 0)
        self.show_entry_box(3, 1)

        self.show_label("Dividend Yield Frequency:", 3, 2)
        self.show_combobox(3, 3, self.dividend_frequency)

        # Row 5
        self.show_label("Expense Ratio:", 4, 0)
        self.show_entry_box(4, 1)

        # Row 6
        self.show_label("Investing Frequency:", 5, 0)
        self.show_combobox(5, 1, self.investing_frequency)

        self.show_label("Investing Amount By Frequency", 5, 2)
        self.show_entry_box(5, 3)

        # Row 7
        self.show_label("Intended year of investing: ", 6, 0)
        self.show_entry_box(6, 1)

        # Row 8
        self.show_button("Calculate", 7, 0)

    def show_label(self, text, row, col, columnspan=1):
        tkinter.Label(self, text=text, bg=BACKGROUND_COLOR,
                      font=('Arial', 10, 'bold')).grid(row=row, column=col, columnspan=columnspan)

    def show_entry_box(self, row, col):
        tkinter.Entry(self, width=20, justify='center').grid(row=row, column=col)

    def show_combobox(self, row, col, value):
        frequency_box = ttk.Combobox(self, value=value, justify='center')
        frequency_box.set(f"{value[0]}")
        frequency_box.grid(row=row, column=col)

    def show_button(self, text, row, col):
        tkinter.Button(self, text=text, width=20, justify='center', command=lambda: [self.get_data_to_controller()]).grid(
            row=row,
            column=col)

    def get_data_to_controller(self):
        self.controller.get_investment_data(self.investment_data)
