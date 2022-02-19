import tkinter
from tkinter import ttk
import os, sys
import datetime
from tkinter import messagebox
from functools import partial

# Resetting the system path.
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")

from controller import main_screen_controller

BACKGROUND_COLOR = 'white'


class MainScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        """This class inherits everything from tkinter.Tk and is responsible for creating a main screen,
        it takes user inputs and send it to controller class."""
        # Initialize main screen controller.
        self.controller = main_screen_controller.MainScreenController()
        self.title('Single Investment Calculator')
        self.geometry('1300x500')
        self.dividend_frequency = ['Monthly', 'Quarterly', 'Yearly']
        self.investing_frequency = ['weekly', 'bi-weekly', 'monthly', 'bi-monthly', 'Quarterly', 'yearly']
        self.entry_boxes = []
        self.comboboxes = []
        self.buttons = []
        self.years_before_now = [datetime.datetime.now().year - year for year in range(0, 41)]
        self.years_before_now.reverse()

        # Disable screen resizable feature.
        self.resizable(False, False)

        self.label_info = [
            {"message": "Investing Title:", "row": 0, "column": 0},
            {"message": "Please enter the following information for the investment", "row": 1, "column": 0,
             "columnspan": 5},
            {"message": "Start Year:", "row": 2, "column": 0},
            {"message": "Start year Price:", "row": 2, "column": 2},
            {"message": "Current Price", "row": 2, "column": 4},
            {"message": "Dividend Yield:", "row": 3, "column": 0},
            {"message": "Dividend Yield Frequency:", "row": 3, "column": 2},
            {"message": "Expense Ratio:", "row": 4, "column": 0},
            {"message": "Investing Frequency:", "row": 5, "column": 0},
            {"message": "Investing Amount By Frequency", "row": 5, "column": 2},
            {"message": "Intended year of investing: ", "row": 6, "column": 0},
        ]

        self.entry_box_info = [
            {"row": 0, "column": 1},
            {"row": 2, "column": 3},
            {"row": 2, "column": 5},
            {"row": 3, "column": 1},
            {"row": 4, "column": 1},
            {"row": 5, "column": 3},
            {"row": 6, "column": 1}
        ]

        self.combobox_info = [
            {"value": self.years_before_now, "row": 2, "column": 1},
            {"value": self.dividend_frequency, "row": 3, "column": 3},
            {"value": self.investing_frequency, "row": 5, "column": 1},
        ]

        self.buttons_info = [
            {"message": "Update", "row": 0, "column": 2, "button_index": 0},
            {"message": "Calculate", "row": 7, "column": 0, "button_index": 1},
            {"message": "Reset", "row": 7, "column": 1, "button_index": 2}
        ]

        for label in self.label_info:
            self.show_label(label['message'], label['row'], label['column'])

        for entry_box in self.entry_box_info:
            self.show_entry_box(entry_box['row'], entry_box['column'])

        for combobox in self.combobox_info:
            self.show_combobox(combobox['value'], combobox['row'], combobox['column'])

        for button in range(0, len(self.buttons_info)):
            self.show_button(self.buttons_info[button]['message'], self.buttons_info[button]['row'],
                             self.buttons_info[button]['column'], self.buttons_info[button]['button_index'])

    def show_label(self, text, row, col, columnspan=1):
        """
        Creates a label and display it on the screen
        :param row: label row index
        :param col: label row index
        """
        tkinter.Label(self, text=text, bg=BACKGROUND_COLOR,
                      font=('Arial', 10, 'bold')).grid(row=row, column=col, columnspan=columnspan)

    def show_entry_box(self, row, col):
        """
        Creates a entry box and display it on the screen
        :param row: entry box row index
        :param col: entry box row index
        """
        entry_box = tkinter.Entry(self, width=20, justify='center')
        entry_box.grid(row=row, column=col)
        self.entry_boxes.append(entry_box)

    def show_combobox(self, value, row, col):
        """
        Creates a combobox and display it on the screen
        :param row: combobox row index
        :param col: combobox coloumn index
        :param value: combobox text value in a list.
        """
        frequency_box = ttk.Combobox(self, value=value, justify='center')
        frequency_box.set("")
        frequency_box.grid(row=row, column=col)
        self.comboboxes.append(frequency_box)

    def show_button(self, text, row, col, i):
        """
        Creates a button and display it on the screen
        :param row: button row index
        :param col: button coloumn index
        :param text: button text
        """
        button = tkinter.Button(self, text=text, width=20, justify='center',
                                command=lambda: self.OnButtonClick(i))

        self.buttons.append(button)
        button.grid(row=row, column=col)

    def OnButtonClick(self, n):
        """Sends user input data to controller"""
        if n == 0:
            self.update_investment_data()
        elif n == 1:
            data = [self.entry_boxes, self.comboboxes]
            if self.controller.is_all_entry_boxes_filled(data):
                messagebox.showwarning("Empty text box", "Please fill all the text entries.")
            else:
                if self.controller.is_float(data, messagebox):
                    self.controller.get_investment_data(data)

            self.controller.get_result()
        elif n == 2:
            self.reset_widget_text()


    def get_result_from_controller(self):
        """Receives data from controller."""
        self.controller.get_result()

    def update_investment_data(self):
        """Automatically update investment data on the screen."""

        # Check if the investment title entry box is empty or not
        self.controller.is_entry_box_empty(self.entry_boxes[0].get(), messagebox)

        self.controller.get_investment_title(self.entry_boxes[0].get())

        # Check if the investment title is valid or not.
        self.controller.is_title_valid(self.entry_boxes[0].get(), messagebox)

        # get automatic data from the internet.
        data = self.controller.get_investment_information()

        self.comboboxes[1].set(data['investment_divident_frequency'])
        self.entry_boxes[3].delete('0', 'end')
        self.entry_boxes[3].insert(0, data['investment_dividend_yield'])
        self.entry_boxes[2].delete('0', 'end')
        self.entry_boxes[2].insert(0, data['investment_current_price'])
        self.entry_boxes[4].delete('0', 'end')
        self.entry_boxes[4].insert(0, data['investment_expense_ratio'])

    def reset_widget_text(self):
        """
        Resets widgets text values.
        :return:
        """
        for text in self.entry_boxes:
            text.delete('0', 'end')
        for box in self.comboboxes:
            box.set('')