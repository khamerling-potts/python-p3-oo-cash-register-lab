#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.prices = []
        self.quantities = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.prices.append(price * quantity)
        self.quantities.append(quantity)
        for i in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if not self.discount == 0:
            self.total -= self.total * 0.2
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.prices[-1]
        for i in range(self.quantities[-1]):
            self.items.pop()
        self.prices.pop()
        self.quantities.pop()
