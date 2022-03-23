from model import calculator
from model import investment_data


class ResultScreenController:
    def __init__(self):
        """This class is responsible for receiving data from the calculator, validating data, and sending data to the
        result screen. """
        self.data = investment_data.InvestmentData()
        self.calculator = calculator.Calculator(self.data)

    def get_result(self):
        """Gets data from the calculator class and sends it main screen."""
        return self.calculator.calculate_investment_total_return()

    def get_investment_data(self, data):
        """parse data and send it to calculator"""

        self.data.parse_data(data)
        self.calculator = calculator.Calculator(self.data)
