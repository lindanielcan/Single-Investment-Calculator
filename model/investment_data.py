from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta


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
        self.investment_dividend_yield = float(data[0][3].get().strip('%'))/100
        self.investment_divident_frequency = (data[1][1].get())
        self.investment_expense_ratio = float(data[0][4].get().strip('%'))/100
        self.investment_frequency = data[1][2].get()
        self.investment_amount_by_frequency = float(data[0][5].get())
        self.investment_intended_years = int(data[0][6].get())

    def get_investment_data(self):
        """
        Scrape https://stockanalysis.com/ to get stock data.
        :return: a list that contains stock data.
        """
        stock_type = 'stocks/'
        url = "https://stockanalysis.com/" + stock_type + self.investment_title + "/dividend/"
        connection = requests.get(url)

        if connection.status_code == 200:
            soup = BeautifulSoup(connection.text, 'html.parser')
            data = soup.find_all('div', 'mt-0.5 text-lg font-semibold bp:text-xl sm:mt-1.5 sm:text-2xl')
            if self.is_market_trading_hour():
                stock_price = soup.find(name='div', class_='p')
            else:
                stock_price = soup.find(name='div', class_='p-ext')
                if stock_price == None:
                    stock_price = soup.find(name='div', class_='p')
            data = [datum.get_text() for datum in data]

            if len(data) == 0:
                return False
            else:
                self.investment_data['investment_dividend_yield'] = data[0]
                self.investment_data['investment_divident_frequency'] = data[3]
                self.investment_data['investment_current_price'] = stock_price.get_text()

        elif connection.status_code == 404:
            stock_type = 'etf/'
            url = "https://stockanalysis.com/" + stock_type + self.investment_title + "/dividend"
            connection = requests.get(url)
            soup = BeautifulSoup(connection.text, 'html.parser')
            data = soup.find_all('div', 'mt-0.5 text-lg font-semibold bp:text-xl sm:mt-1.5 sm:text-2xl')
            data = [datum.get_text() for datum in data]

            if self.is_market_trading_hour():
                stock_price = soup.find(name='div', class_='p')
            else:
                stock_price = soup.find(name='div', class_='p-ext')
                if stock_price == None:
                    stock_price = soup.find(name='div', class_='p')
            if len(data) == 0:
                return False
            else:
                self.investment_data['investment_dividend_yield'] = data[0]
                self.investment_data['investment_divident_frequency'] = data[3]
                self.investment_data['investment_current_price'] = stock_price.get_text()

        connection.close()

        self.get_expense_ratio()

        return self.investment_data

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

    def get_expense_ratio(self):
        """Get the expense ratio for the investment."""

        url = "https://stockanalysis.com/etf/" + self.investment_title
        new_connection = requests.get(url)

        self.investment_data['investment_expense_ratio'] = ''

        if new_connection.status_code == 200:
            soup = BeautifulSoup(new_connection.text, 'html.parser')

            self.investment_data['investment_expense_ratio'] = (soup.find_all('td',
                                                                              'py-[1px] sm:py-2 px-1 whitespace-nowrap text-left sm:text-right text-base sm:text-small font-semibold')[
                                                                    2].get_text())

        else:
            self.investment_data['investment_expense_ratio'] = 0
