#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount = 0) -> None:
        # self.quantity = quantity
        # self.price = price
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity = 1):
        i = 0
        while i < quantity:
            self.items.append(title)
            i += 1 
        
        self.amount = price * quantity
        self.total += self.amount
        self.quantity = quantity

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total -= self.total *self.discount/100
            print(f"After the discount, the total comes to ${int(self.total)}.")
    
    def void_last_transaction(self):
        self.total -= self.amount

# stuff = CashRegister(10)
# stuff.add_item("onions",40,4)
# print(stuff.items)