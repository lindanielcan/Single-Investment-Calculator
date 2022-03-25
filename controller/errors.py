from datetime import datetime


class Errors:
    def __init__(self):
        """This class is responsible to handle errors or show exceptions."""

    def check_empty(self, data):
        """Check if an entry is empty or not"""

        try:
            new_data = 10 / len(str(data))
            return True
        except ZeroDivisionError:
            return False

    def is_float(self, data):
        """Check if an entry is float or not"""
        try:
            new_data = float(data)
            return True
        except ValueError:
            return False

    def is_integer(self, data):
        """Check if an entry is float or not"""
        try:
            new_data = int(data)
            return True
        except ValueError:
            return False

    def is_not_negative(self, data):
        """Checks to see if the data is negative or not"""
        try:
            if data < 0:
                return True
        except TypeError:
            return False

    def show_warning_for_code_429(self, code, messagebox):
        if code == 429:
            messagebox.showwarning("Please wait a little and try to update the data again.")
