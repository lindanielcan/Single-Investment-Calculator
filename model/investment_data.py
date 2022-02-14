class InvestmentData:
    def __init__(self):
        """This class manages data."""
        self.data = []
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

    def parse_data(self, data):
        """Gets the data from the controller and parse it."""
        self.data = (data)
        self.investment_title = self.data[0][0].get()
        self.investment_start_year = self.data[1][0].get()
        self.investment_start_year_price = self.data[0][1].get()
        self.investment_current_price = self.data[0][2].get()
        self.investment_dividend_yield = self.data[0][3].get()
        self.investment_divident_frequency = self.data[1][1].get()
        self.investment_expense_ratio = self.data[0][4].get()
        self.investment_frequency = self.data[1][2].get()
        self.investment_amount_by_frequency = self.data[0][5].get()
        self.investment_intended_years = self.data[0][6].get()
