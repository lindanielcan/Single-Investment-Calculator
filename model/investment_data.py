
import requests
from datetime import datetime

class InvestmentData:
    def __init__(self):
        """This class manages data."""
        self.data = {}
        self.investment_title = ''
        self.investment_start_year = 0
        self.investment_start_year_price = 0
        self.investment_current_price = 0
        self.investment_dividend_yield = 0
        self.investment_divident_frequency = 0
        self.investment_expense_ratio = 0
        self.investment_frequency = 0
        self.investment_amount_by_frequency = 0
        self.investment_intended_years = 0
        self.current_time = datetime.now().time()
        self.investment_data = {}


    def parse_data(self, data):
        """Gets the data from the controller and parse it."""
        self.investment_title = data[0][0].get()
        self.investment_start_year = int(data[1][0].get())
        self.investment_start_year_price = float(data[0][1].get())
        self.investment_current_price = float(data[0][2].get())
        self.investment_dividend_yield = float(data[0][3].get().strip('%')) / 100
        self.investment_divident_frequency = (data[1][1].get())
        self.investment_expense_ratio = float(data[0][4].get().strip('%')) / 100
        self.investment_frequency = data[1][2].get()
        self.investment_amount_by_frequency = float(data[0][5].get())
        self.investment_intended_years = int(data[0][6].get())

    def is_market_trading_hour(self):
        """Finds out if current time during market trading hour or not."""
        current_time = datetime.now().time()
        current_time_in_second = current_time.hour * 60 * 60 + current_time.minute * 60 + current_time.second
        pre_market_time = 9 * 60 * 60 + 30 * 60
        after_hour = 16 * 60 * 60
        if 0 <= datetime.now().weekday() <= 4 and pre_market_time <= current_time_in_second <= after_hour:
            return True
        else:
            return False
