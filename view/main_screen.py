import tkinter
from tkinter import ttk
import os, sys
import datetime
from tkinter import messagebox

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
        self.geometry('1000x500')
        self.dividend_frequency = ['monthly', 'Quarterly', 'yearly']
        self.investing_frequency = ['weekly', 'bi-weekly', 'monthly', 'bi-monthly', 'Quarterly', 'yearly']
        self.entry_boxes = []
        self.comboboxes = []
        self.years_before_now = [datetime.datetime.now().year - year for year in range(0, 41)]
        self.years_before_now.reverse()

        # Set the screen to not resizable.
        self.resizable(False, False)

        # Row 1 content
        self.show_label("Investing Title:", 0, 0)
        (self.show_entry_box(0, 1))
        self.show_button('Update', 0, 1)

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

    def show_combobox(self, row, col, value):
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

    def show_button(self, text, row, col):
        """
        Creates a button and display it on the screen
        :param row: button row index
        :param col: button coloumn index
        :param text: button text
        """
        button = tkinter.Button(self, text=text, width=20, justify='center',
                                command=lambda: [self.get_entry_data_to_controller(),
                                                 self.get_result_from_controller()])
        button.grid(row=row, column=col)

    def get_entry_data_to_controller(self):
        """Sends user input data to controller"""
        data = [self.entry_boxes, self.comboboxes]
        if self.controller.is_all_entry_boxes_filled(data):
            messagebox.showwarning("Empty text box", "Please fill all the text entries.")
        else:
            if self.controller.is_float(data, messagebox):
                self.controller.get_investment_data(data)

    def get_result_from_controller(self):
        """Receives data from controller."""
        self.controller.get_result()

    def update_investment_data(self):
        """Automatically Show investment data on the screen."""
        pass