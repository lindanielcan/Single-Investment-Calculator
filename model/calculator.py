from datetime import datetime

from model import investment_data


class Calculator:
    def __init__(self):
        """Calculator calculates investment data."""
        self.current_year = datetime.now().year
        self.investment_data = investment_data.InvestmentData()

    def is_leap_year(self, year):
        """
        :param year: number of years
        :return: if the inputted year is a leap year or not.
        """
        if year % 4 == 0:
            return True
        else:
            return False

    def number_of_days(self, year):
        """
        :param year: number of years
        :return: number of weeks between now and the in the inputted years.
        """
        current_year = int(datetime.now().year)
        future_year = current_year + year
        total_days = 0

        for n_year in range(current_year, future_year):
            if self.is_leap_year(n_year):
                total_days += 366
            else:

                total_days += 365

        return total_days

    def get_yearly_average_growth_rate(self):
        """Calculates average growth rate of an investment."""
        # GR = [(ending value) / (beginning value)] ^ (1 / n) - 1
        number_of_years = self.current_year - self.investment_data.investment_start_year
        yearly_growth_rate = (
                                     self.investment_data.investment_current_price - self.investment_data.investment_start_year_price) ** (
                                     1 / number_of_years) - 1
        return yearly_growth_rate

    def get_weekly_average_growth_rate(self):
        """Returns average weekly growth rate"""
        return self.get_yearly_average_growth_rate() / (
                self.get_days() / self.investment_data.investment_intended_years / 7)

    def get_days(self):
        """Returns the number of days that is equal to the years of intended investment."""
        total_of_days = 0
        for year in range(0, self.investment_data.investment_intended_years):
            if self.is_leap_year(self.current_year + year):
                total_of_days += 366
            else:
                total_of_days += 365
        return total_of_days

    def calculate_investment_total_return(self):
        """Calculates investment total return from the data received"""
        total_investment_return = 0
        days = self.get_days()
        for day in range(1, days + 1):
            # when day % 7 == 0, its a week.
            if day % 7 == 0:
                total_investment_return += self.investment_data.investment_amount_by_frequency * (
                        (self.get_weekly_average_growth_rate() + 1) ** (days - day))
            # when day % 30 == 0, its a season.
            if day % 91 == 0:
                pass
            # when day % 365 == 0, its a year.
            if day % 365 == 0:
                pass

        return total_investment_return
