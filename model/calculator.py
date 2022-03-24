from datetime import datetime


class Calculator:
    def __init__(self, investment_data):
        """Calculator calculates investment data."""
        self.current_year = datetime.now().year
        self.investment_data = investment_data
        self.results = {}
        self.total_expense_fee_paid = 0
        self.total_dividend_received = 0
        self.total_money_if_not_invest = 0

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
        number_of_years = float(self.current_year) - self.investment_data.investment_start_year
        return (self.investment_data.investment_current_price / self.investment_data.investment_start_year_price) ** (
                1 / number_of_years) - 1

    def get_days(self):
        """Returns the number of days that is equal to the years of intended investment."""
        total_of_days = 0

        for year in range(0, self.investment_data.investment_intended_years):
            if self.is_leap_year(self.current_year + year):
                total_of_days += 366
            else:
                total_of_days += 365
        return total_of_days

    def investment_return_with_dividend(self, total_investment_return, day):
        """Conpound the investment with dividend."""
        if self.investment_data.investment_dividend_yield != 0:

            if self.investment_data.investment_divident_frequency == 'monthly'.title():
                if day % 30 == 0:
                    total_investment_return_before_dividend = total_investment_return
                    total_investment_return *= ((self.investment_data.investment_dividend_yield / 12) + 1)

                    self.total_dividend_received = self.total_dividend_received + (
                            total_investment_return - total_investment_return_before_dividend)

            elif self.investment_data.investment_divident_frequency == 'Quarterly'.title():
                if day % 91 == 0:
                    total_investment_return_before_dividend = total_investment_return
                    total_investment_return *= ((self.investment_data.investment_dividend_yield / 4) + 1)
                    self.total_dividend_received = self.total_dividend_received + (
                            total_investment_return - total_investment_return_before_dividend)

            elif self.investment_data.investment_divident_frequency == 'yearly'.title():
                if day % 365 == 0:
                    total_investment_return_before_dividend = total_investment_return
                    total_investment_return *= ((self.investment_data.investment_dividend_yield / 1) + 1)
                    self.total_dividend_received = self.total_dividend_received + (
                            total_investment_return - total_investment_return_before_dividend)

        return total_investment_return

    def calculate_weekly_investment(self, days, investment_frequency, number_average_growth_rate_per_frequency):
        """
        Returns total investment return when user invest weekly
        :param days: integer - total of days
        :param investment_frequency: integer - how often does user invest ie. 7 - weekly, 14 - bi-weekly, 30 - monthly
        :param number_average_growth_rate_per_frequency:
        :return: integer - total investment return
        """
        total_investment_return = 0
        # The total investment will be compounded by dividend, and it may slightly vary bases on how dividend is
        # being paid.
        for day in range(0, days):
            # Total returns of each week investment should be different, amount of investment from each week is
            # compounded differently, The initial investment in theory should be compounded the most.
            if day % investment_frequency == 0:
                total_investment_return += self.investment_data.investment_amount_by_frequency * (
                        ((self.get_yearly_average_growth_rate() / number_average_growth_rate_per_frequency) + 1) ** (
                        (days - day) / investment_frequency))
            # Every 365 days, the users pays certain amount of fees(etf,..) bases the amount of total value they are
            # holding, if the investment is a stock not a etf or mutual fund, then expense ratio would 0.
            if day % 365 == 0:
                # print(total_investment_return)
                total_investment_return = self.investment_return_with_expense_ratio(total_investment_return)
                # print(total_investment_return)
            if self.investment_data.investment_dividend_yield != 'n/a' and self.investment_data.investment_divident_frequency != 'n/a' and \
                    self.investment_data.investment_divident_frequency != 'Unspecified':
                total_investment_return = self.investment_return_with_dividend(total_investment_return, day)

        return total_investment_return

    def calculate_investment_total_return(self):
        """
        Calculates investment total return with various scenarios
        :return: investment total return
        """
        total_investment_return = 0
        days = self.get_days()

        # Different investing case scenarios
        # user invests weekly
        if self.investment_data.investment_frequency == 'weekly':
            total_investment_return = self.calculate_weekly_investment(days, 7, 52)
            # Calcalates the tatal amount of money saved up in years if not invested.
            self.total_money_if_not_invest = self.investment_data.investment_intended_years * self.investment_data.investment_amount_by_frequency * 52
        # user invests bi-weekly
        elif self.investment_data.investment_frequency == 'bi-weekly':
            total_investment_return = self.calculate_weekly_investment(days, 14, 26)
            self.total_money_if_not_invest = self.investment_data.investment_intended_years * self.investment_data.investment_amount_by_frequency * 26
        # user invests monthly
        elif self.investment_data.investment_frequency == 'monthly':
            total_investment_return = self.calculate_weekly_investment(days, 30, 12)
            self.total_money_if_not_invest = self.investment_data.investment_intended_years * self.investment_data.investment_amount_by_frequency * 12
        # user invests bi-monthly
        elif self.investment_data.investment_frequency == 'bi-monthly':
            total_investment_return = self.calculate_weekly_investment(days, 61, 6)
            self.total_money_if_not_invest = self.investment_data.investment_intended_years * self.investment_data.investment_amount_by_frequency * 6
        # user invests quarterly
        elif self.investment_data.investment_frequency == 'Quarterly':
            total_investment_return = self.calculate_weekly_investment(days, 91, 4)
            self.total_money_if_not_invest = self.investment_data.investment_intended_years * self.investment_data.investment_amount_by_frequency * 4
        # user invests yearly
        elif self.investment_data.investment_frequency == 'yearly':
            total_investment_return = self.calculate_weekly_investment(days, 365, 1)
            self.total_money_if_not_invest = self.investment_data.investment_intended_years * self.investment_data.investment_amount_by_frequency * 1

        return total_investment_return

    def investment_return_with_expense_ratio(self, total_investment_return):
        """Calculates total return after paying for fees"""
        if self.investment_data.investment_expense_ratio != 0:
            total_investment_return_before_paying_expense_fee = total_investment_return
            total_investment_return *= (1 - self.investment_data.investment_expense_ratio)
            self.total_expense_fee_paid += (total_investment_return_before_paying_expense_fee - total_investment_return)
        return total_investment_return

    def get_results(self):
        """
        Gets various results.
        :return: a dictionary containing different results.
        """
        years = {self.investment_data.investment_intended_years}
        total_return = round(self.calculate_investment_total_return(), 2)

        self.results[
            'yearly_average_growth'] = f"""The yearly average growth of your investment in  years is likely to be {"{:.2f}".format(((round(self.get_yearly_average_growth_rate(), 4)) * 100))}%."""
        self.results[
            'yearly_average_growth_with_dividend'] = f"The yearly average growth of your investment with dividend " \
                                                     f"included in  years is " \
                                                     f"""estimated to be {"{:.2f}".format(round((self.get_yearly_average_growth_rate() * (self.investment_data.investment_dividend_yield + 1)), 4) * 100)}%."""
        self.results[
            'expense_fee_paid'] = f"The total amount of money will be charged for the expense ratio by the investment " \
                                  f"over {years} years would be ${round(self.total_expense_fee_paid, 2)}."
        self.results[
            'total_dividend_received'] = f"The total amount of dividend you will receive from the investment is " \
                                         f"estimated to be ${round(self.total_dividend_received, 2)}."

        self.results[
            'total_investment_return'] = f"The total return of your investment is estimated to be ${total_return} vs ${round(self.total_money_if_not_invest, 2)} you didn't invest"

        return self.results
