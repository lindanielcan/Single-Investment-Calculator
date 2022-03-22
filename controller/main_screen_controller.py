from model import calculator
from model import investment_data
from model import scraper

class MainScreenController:
    def __init__(self):
        """This class receives data from the main screen, sends data to model files,
        and receives results from calculator class."""

        self.investment_data = investment_data.InvestmentData()
        self.scraper = scraper.Scraper(self.investment_data)
        self.calculator = calculator.Calculator(self.investment_data)


    def get_investment_data(self, data):
        """parse data and send it to calculator"""

        self.investment_data.parse_data(data)

    def get_result(self):
        """Gets data from the calculator class and sends it main screen."""
        return self.calculator.calculate_investment_total_return()

    def is_all_entry_boxes_filled(self, data):
        """Checks to see if all the entry boxes were filled."""
        for datum in data:
            for item in datum:
                if len(item.get()) == 0:
                    return True

    def is_float(self, data, messagebox):
        """Checks if the data is convertible to float or not."""
        new_data = [item.get() for item in data[0]]
        new_data.pop(0)
        new_data.append(data[1][0].get())
        new_data[2] = new_data[2].strip('%')
        new_data[3] = new_data[3].strip('%')

        try:
            for item in new_data:
                item = float(item)
        except ValueError:
            messagebox.showwarning("Please check the value", "Please check the value you inputted.")
        else:
            return True

    def get_investment_title(self, title):
        """
        Gets investment title from the main screen and send it to investment_data
        :param title: investment_title
        :return: a dictionary containing investment information
        """
        # If the title entry is empty, prompt a window telling the user to enter the investment title.
        self.investment_data.investment_title = title

    def is_title_valid(self, title, message_box):
        """Checks to see if the investment title is valid or not"""
        if len(title) != 0 and self.scraper.get_investment_data() == False:
            message_box.showwarning("Invalid investment title",
                                    "Please enter a valid investment title or enter following information manually")

    def get_investment_information(self):
        """Send investment data from investment_data to the screen"""

        return self.scraper.get_investment_data()

    def is_entry_box_empty(self, title, message_box):
        """Checks to see if the investment title entry box is empty or not, if yes, send a message"""

        if len(title) == 0:
            message_box.showwarning("Empty entry", "In order to update investment data, please enter investment title")

