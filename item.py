class item:
    def __init__(self, name, price = 0.0, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show(self):
        return f"Name: {self.name}, price: ${self.price}, Stock: {self.quantity}"

    def restock(self, q):
        self.quantity += q

    def sold(self, s = 1):
        if(self.quantity > 0):
            self.quantity -= s
            
        else:
            print(f"{self.name} sold out" )