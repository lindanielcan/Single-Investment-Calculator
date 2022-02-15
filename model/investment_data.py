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

    def parse_data(self, data):
        """Gets the data from the controller and parse it."""
        self.investment_title = data[0][0].get()
        self.investment_start_year = int(data[1][0].get())
        self.investment_start_year_price = float(data[0][1].get())
        self.investment_current_price = float(data[0][2].get())
        self.investment_dividend_yield = float(data[0][3].get())
        self.investment_divident_frequency = (data[1][1].get())
        self.investment_expense_ratio = float(data[0][4].get())
        self.investment_frequency = data[1][2].get()
        self.investment_amount_by_frequency = float(data[0][5].get())
        self.investment_intended_years = int(data[0][6].get())
