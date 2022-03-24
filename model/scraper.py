import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, investment_data):
        """This class is responsible to scrape data from the internet."""

        # pass a default browser setting so the visiting site won't block the user from scraping data.
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }
        self.data = investment_data

    def get_investment_data(self):
        """
        Scrape https://stockanalysis.com/ to get stock data.
        :return: a list that contains stock data.
        """

        stock_type = 'stocks/'
        url = "https://stockanalysis.com/" + stock_type + self.data.investment_title + "/dividend/"

        connection = requests.get(url, headers=self.headers)
        print(connection.status_code)
        if connection.status_code == 200:

            soup = BeautifulSoup(connection.text, 'html.parser')
            data = soup.find_all('div', 'mt-0.5 text-lg font-semibold bp:text-xl sm:mt-1.5 sm:text-2xl')

            if self.data.is_market_trading_hour():
                stock_price = soup.find(name='div', class_='p')
            else:
                stock_price = soup.find(name='div', class_='p-ext')
                if stock_price == None:
                    stock_price = soup.find(name='div', class_='p')
            data = [datum.get_text() for datum in data]

            if len(data) == 0:
                return False
            else:
                self.data.investment_data['investment_dividend_yield'] = data[0]
                self.data.investment_data['investment_divident_frequency'] = data[3]
                self.data.investment_data['investment_current_price'] = stock_price.get_text()

        elif connection.status_code == 404:
            stock_type = 'etf/'
            url = "https://stockanalysis.com/" + stock_type + self.data.investment_title + "/dividend"
            connection = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(connection.text, 'html.parser')
            data = soup.find_all('div', 'mt-0.5 text-lg font-semibold bp:text-xl sm:mt-1.5 sm:text-2xl')
            data = [datum.get_text() for datum in data]

            if self.data.is_market_trading_hour():
                stock_price = soup.find(name='div', class_='p')
            else:
                stock_price = soup.find(name='div', class_='p-ext')
                if stock_price == None:
                    stock_price = soup.find(name='div', class_='p')
            if len(data) == 0:
                return False
            else:
                self.data.investment_data['investment_dividend_yield'] = data[0]
                self.data.investment_data['investment_divident_frequency'] = data[3]
                self.data.investment_data['investment_current_price'] = stock_price.get_text()

        connection.close()

        self.get_expense_ratio()
        self.get_history_data()

        return self.data.investment_data

    def get_expense_ratio(self):
        """Get the expense ratio for the investment."""

        url = "https://stockanalysis.com/etf/" + self.data.investment_title
        new_connection = requests.get(url, headers=self.headers)

        self.data.investment_data['investment_expense_ratio'] = ''

        if new_connection.status_code == 200:
            soup = BeautifulSoup(new_connection.text, 'html.parser')

            self.data.investment_data['investment_expense_ratio'] = (soup.find_all('td',
                                                                                   'py-[1px] sm:py-2 px-1 whitespace-nowrap text-left sm:text-right text-base sm:text-small font-semibold')[
                                                                         2].get_text())

        else:
            self.data.investment_data['investment_expense_ratio'] = 0

    def get_history_data(self):
        """Gets the price of the year for the investment."""

        url = "https://www.macrotrends.net/stocks/charts/" + self.data.investment_title + "/at-t/stock-price-history"
        new_connection = requests.get(url, headers=self.headers)

        if new_connection.status_code == 200:
            soup = BeautifulSoup(new_connection.text, 'html.parser')
            # Storing all the historical price data into a list.
            my_list = soup.find_all("td")

            for item in my_list:
                if self.data.investment_start_year in item:
                    self.data.investment_data['investment_start_year_price'] = round(float(my_list[my_list.index(item) + 1].get_text().strip('>')),2)

        else:
            return None

        new_connection.close()
