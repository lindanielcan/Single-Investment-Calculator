from model import calculator
from model import investment_data
from model import scraper
from controller import errors


class MainScreenController:
    def __init__(self):
        """This class receives data from the main screen, sends data to model files,
        and receives results from calculator class."""

        self.investment_data = investment_data.InvestmentData()
        self.scraper = scraper.Scraper(self.investment_data)
        self.errors = errors.Errors()
        self.messages_for_entry_box = [
            "Please check the investment title input is filled and valid.",
            "Please check the start year price.",
            "Please check the current price.",
            "Please check the dividend yield.",
            "Please check the expense ratio.",
            "Please check the investing amount by frequency.",
            "Please check the intended year of investing."
        ]

        self.messages_for_combobox = [
            "Please select a proper start year.",
            "Please select a proper dividend yield frequency.",
            "Please select a proper investing frequency."
        ]

    def get_investment_title_and_start_year(self, title, year):
        """
        Gets investment title from the main screen and send it to investment_data
        :param title: investment_title
        :param title: investment start year
        """
        # If the title entry is empty, prompt a window telling the user to enter the investment title.
        self.investment_data.investment_title = title
        self.investment_data.investment_start_year = year

    def get_investment_information(self):
        """Send investment data from investment_data to the screen"""

        return self.scraper.get_investment_data()

    def is_all_inputs_valid(self, data, messagebox):
        """
        Checks to see if all the inputs are valid.
        :param data: List - a list containing text value
        :param messagebox: tkinter.messagebox
        :return: Boolean - if all the inputs are filled and valid, then it returns true.
        """
        is_valid = True

        for index in range(0, len(data[0])):
            is_valid = self.check_entry(index, data, messagebox)
            if not is_valid:
                break

        for index in range(0, len(data[1])):
            is_valid = self.check_combobox(index, data, messagebox)
            if not is_valid:
                break

        return is_valid

    def check_combobox(self, index, data, messagebox):
        """Chech each combobox value"""
        if not self.errors.check_empty(data[1][index]):
            messagebox.showwarning(message=self.messages_for_combobox[index])
            return False
        else:
            return True

    def check_entry(self, index, data, messagebox):
        """
        Check each entry in the main screen.
        :param index: int - list index
        :param data: list - widget data
        :param messagebox:
        :return: boolean - If all the data are filled and valid, return True
        """
        if index == 0:
            if not self.errors.check_empty(data[0][index]):
                messagebox.showwarning(message=self.messages_for_entry_box[index])
                return False
            else:
                return True
        else:
            if self.errors.check_empty(data[0][index]) == False and self.errors.is_float(
                    data[0][index]) == False and self.errors.is_not_negative(data[0][index]) == False:
                messagebox.showwarning(message=self.messages_for_entry_box[index])
                return False
            else:
                return True

    def connection_warning(self, messagebox):
        """shows messages for different connection code."""
        self.errors.show_warning_for_code_429(self.scraper.connection_code, messagebox)
