class MainScreenController:
    def __init__(self):
        self.data = []

    def get_investment_data(self, data):
        self.data = data
        print(data)