from model import calculator
from model import investment_data


class MainScreenController:
    def __init__(self):
        """This class receives data from the main screen, sends data to model files,
        and receives results from calculator class."""
        self.calculator = calculator.Calculator()
        self.investment_data = investment_data.InvestmentData()

    def get_investment_data(self, data):
        """Send data."""
        self.investment_data.parse_data(data)

    def get_result(self):
        """Gets data from the calculator class and sends it main screen."""
        return self.calculator.calculate_investment_total_return()
