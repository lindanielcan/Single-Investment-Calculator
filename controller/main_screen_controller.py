from model import calculator
from model import investment_data


class MainScreenController:
    def __init__(self):
        """This class receives data from the main screen, sends data to model files,
        and receives results from calculator class."""

        self.investment_data = investment_data.InvestmentData()
        self.calculator = calculator.Calculator(self.investment_data)

    def get_investment_data(self, data):
        """parse data and send it to calculator"""

        self.investment_data.parse_data(data)

    def get_result(self):
        """Gets data from the calculator class and sends it main screen."""
        print(self.calculator.calculate_investment_total_return())
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
        try:
            for item in new_data:
                item = float(item)
        except ValueError:
            messagebox.showwarning("Please check the value", "Please check the value you inputted.")
        else:
            return True
