import tkinter
from tkinter import ttk
import os, sys
import datetime
from tkinter import messagebox
from PIL import ImageTk, Image
from view import result_screen

# Resetting the system path.
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")

from controller import main_screen_controller
from controller import result_screen_controller

BACKGROUND_COLOR = '#BFFFF0'


class MainScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        """This class inherits everything from tkinter.Tk and is responsible for creating a main screen,
        it takes user inputs and send it to controller class."""
        self.title('Single Investment Calculator')
        self.geometry('550x500')
        self.config(bg=BACKGROUND_COLOR)

        self.main_screen_controller = main_screen_controller.MainScreenController()
        self.result_screen_controller = result_screen_controller.ResultScreenController()
        self.result_screen = result_screen.ResultScreen(self)

        self.dividend_frequency = ['Monthly', 'Quarterly', 'Yearly']
        self.investing_frequency = ['weekly', 'bi-weekly', 'monthly', 'bi-monthly', 'Quarterly', 'yearly']
        self.entry_boxes = []
        self.comboboxes = []
        self.buttons = []

        self.years_before_now = [datetime.datetime.now().year - year for year in range(0, 41)]
        self.years_before_now.reverse()

        # creats a canva to store and display an image.
        self.my_canva = tkinter.Canvas(self, bg=BACKGROUND_COLOR, width=550, height=150,
                                       highlightbackground=BACKGROUND_COLOR)
        self.img = Image.open("view/images/investing.png")
        self.img = self.img.resize((100, 100), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.img)
        self.my_canva.create_image(240, 15, image=self.new_image, anchor='nw')
        self.my_canva.grid(row=0, column=0, columnspan=2, padx=22.5)

        # Disable screen resizable feature.
        self.resizable(False, False)

        # Storing label information in a list.
        self.label_info = [
            {"message": "Investing Title:", "row": 1, "column": 0},
            {"message": "Please enter the following information for the investment:", "row": 3, "column": 0,
             "columnspan": 2},
            {"message": "Start Year:", "row": 2, "column": 0},
            {"message": "Start year Price:", "row": 5, "column": 0},
            {"message": "Current Price:", "row": 6, "column": 0},
            {"message": "Dividend Yield:", "row": 7, "column": 0},
            {"message": "Dividend Yield Frequency:", "row": 8, "column": 0},
            {"message": "Expense Ratio:", "row": 9, "column": 0},
            {"message": "Investing Frequency:", "row": 10, "column": 0},
            {"message": "Investing Amount By Frequency:", "row": 11, "column": 0},
            {"message": "Intended year of investing:", "row": 12, "column": 0},
        ]

        # Storing entry box information in a list.
        self.entry_box_info = [
            {"row": 1, "column": 1},
            {"row": 5, "column": 1},
            {"row": 6, "column": 1},
            {"row": 7, "column": 1},
            {"row": 9, "column": 1},
            {"row": 11, "column": 1},
            {"row": 12, "column": 1}
        ]

        # Storing combo box information in a list.
        self.combobox_info = [
            {"value": self.years_before_now, "row": 2, "column": 1},
            {"value": self.dividend_frequency, "row": 8, "column": 1},
            {"value": self.investing_frequency, "row": 10, "column": 1},
        ]

        # Storing button information in a list.
        self.buttons_info = [
            {"message": "Update", "row": 4, "column": 1, "button_index": 0},
            {"message": "Calculate", "row": 13, "column": 0, "button_index": 1},
            {"message": "Reset", "row": 13, "column": 1, "button_index": 2}
        ]

        # running loops through lists to display widgets.
        for label in self.label_info:
            if self.label_info.index(label) != 1:
                self.show_label(label['message'], label['row'], label['column'], tkinter.E)
            else:
                self.show_label(label['message'], label['row'], label['column'], tkinter.N, label['columnspan'])

        for entry_box in self.entry_box_info:
            self.show_entry_box(entry_box['row'], entry_box['column'])

        for combobox in self.combobox_info:
            self.show_combobox(combobox['value'], combobox['row'], combobox['column'])

        for button in range(0, len(self.buttons_info)):
            if button == 0:
                self.show_button(self.buttons_info[button]['message'], self.buttons_info[button]['row'],
                                 self.buttons_info[button]['column'], self.buttons_info[button]['button_index'],
                                 tkinter.W)
            elif button == 1:
                self.show_button(self.buttons_info[button]['message'], self.buttons_info[button]['row'],
                                 self.buttons_info[button]['column'], self.buttons_info[button]['button_index'],
                                 tkinter.N)
            elif button == 2:
                self.show_button(self.buttons_info[button]['message'], self.buttons_info[button]['row'],
                                 self.buttons_info[button]['column'], self.buttons_info[button]['button_index'],
                                 tkinter.W)

    def show_label(self, text, row, col, button_widget_direction, columnspan=1):
        """
        Creates a label and display it on the screen
        :param row: label row index
        :param col: label row index
        """
        tkinter.Label(self, text=text, bg=BACKGROUND_COLOR, anchor="w",
                      font=('Arial', 10, 'bold',)).grid(row=row, column=col, columnspan=columnspan,
                                                        sticky=button_widget_direction)

    def show_entry_box(self, row, col):
        """
        Creates a entry box and display it on the screen
        :param row: entry box row index
        :param col: entry box row index
        """
        entry_box = tkinter.Entry(self, width=20, justify='center')
        entry_box.grid(row=row, column=col, sticky=tkinter.W)
        self.entry_boxes.append(entry_box)

    def show_combobox(self, value, row, col):
        """
        Creates a combobox and display it on the screen
        :param row: combobox row index
        :param col: combobox coloumn index
        :param value: combobox text value in a list.
        """
        frequency_box = ttk.Combobox(self, value=value, justify='center', width=17)
        frequency_box.set("")
        frequency_box.grid(row=row, column=col, sticky=tkinter.W)
        self.comboboxes.append(frequency_box)

    def show_button(self, text, row, col, i, button_widget_direction):
        """
        Creates a button and display it on the screen
        :param row: button row index
        :param col: button coloumn index
        :param text: button text
        :param i: used to assign identity to each button.
        """
        button = tkinter.Button(self, text=text, width=10, justify='center',
                                command=lambda: self.OnButtonClick(i))

        self.buttons.append(button)
        button.grid(row=row, column=col, sticky=button_widget_direction)

    def OnButtonClick(self, n):
        """
        Performs functions when a specific button is pressed.
        :param n: button identity.
        """
        # Fills in investment data when update button is pressed.
        if n == 0:
            self.update_button_pressed()

        # Sends data from the screen to the controller when calculate button is pressed.
        elif n == 1:
            self.calculate_button_pressed()

        elif n == 2:
            self.reset_button_pressed()

    def update_button_pressed(self):
        """When update button is clicked, automatically update investment data on the screen."""

        # Check if the investment title entry box is empty or not
        self.main_screen_controller.is_entry_box_empty(self.entry_boxes[0].get(), messagebox)

        self.main_screen_controller.get_investment_title_and_start_year(self.entry_boxes[0].get(),
                                                                        self.comboboxes[0].get())

        # Check if the investment title is valid or not.
        self.main_screen_controller.is_title_valid(self.entry_boxes[0].get(), messagebox)

        # get automatic data from the internet.
        data = self.main_screen_controller.get_investment_information()

        self.comboboxes[1].set(data['investment_divident_frequency'])
        self.entry_boxes[1].delete('0', 'end')
        self.entry_boxes[1].insert(0, data['investment_start_year_price'])
        self.entry_boxes[3].delete('0', 'end')
        self.entry_boxes[3].insert(0, data['investment_dividend_yield'])
        self.entry_boxes[2].delete('0', 'end')
        self.entry_boxes[2].insert(0, data['investment_current_price'])
        self.entry_boxes[4].delete('0', 'end')
        self.entry_boxes[4].insert(0, data['investment_expense_ratio'])

    def reset_button_pressed(self):
        """
        Resets widgets text values.
        """
        for text in self.entry_boxes:
            text.delete('0', 'end')
        for box in self.comboboxes:
            box.set('')

    def calculate_button_pressed(self):
        """
        Opens result screen and show results.
        """
        data = [self.entry_boxes, self.comboboxes]
        # Checks if all the boxes were filled.
        if self.main_screen_controller.is_all_entry_boxes_filled(data):
            messagebox.showwarning("Empty text box", "Please fill all the text entries.")
        else:
            # Validates data, if data is valid, then send it to result screen controller.
            if self.main_screen_controller.is_float(data, messagebox):
                self.result_screen.set_investment_data(data)
                self.result_screen.open()
