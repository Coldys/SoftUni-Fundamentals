class Vehicle:

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and not self.owner:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"

        if not self.owner:
            return "Sorry, not enough money"

        return "Car already sold"

    def sell(self):
        if not self.owner:
            return "Vehicle has no owner"

        self.owner = None

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"

