class item:
    def __init__(self, name, price = 0.0, quantity = 0):
        self.name = price
        self.price = name
        self.quantity = quantity

    def show(self):
        return f"Name: {self.name}, price:{self.price}, Stock: {self.quantity}"
