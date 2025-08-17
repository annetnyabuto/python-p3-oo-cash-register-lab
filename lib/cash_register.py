#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = [] 

  def apply_discount(self):
    if self.discount:
        self.total = int(self.total * ((100 - self.discount) / 100))
        print(f"After the discount, the total comes to ${self.total}.")
    else:
        print("There is no discount to apply.")

  def add_item(self, title, price, quantity = 1):
    self.last_transaction.append({"title": title, "price": price * quantity, "quantity": quantity})
    
    self.total += price * quantity 

    for _ in range(quantity):
      self.items.append(title)

  def list_with_multiples(self):
    return self.items

  def void_last_transaction(self):
    if self.last_transaction:
      self.total -= self.last_transaction[-1]["price"] 
      
      for _ in range(self.last_transaction[-1]["quantity"]):
        self.items.pop()
      
      self.last_transaction.pop()
    else:
        print("You have no transactions yet. Call add_item to include one.")


cashRegister = CashRegister(20)
cashRegister.add_item("eggs", 3, 4)
cashRegister.add_item("eggs", 3)
cashRegister.add_item("macbook air", 1000)
print(cashRegister.total)

print(cashRegister.items)
print(f"Last transaction is: {cashRegister.last_transaction}")
print(f"Last item transacted: {cashRegister.last_transaction[-1]}")
print(f"Total before discount: {cashRegister.total}")

print(cashRegister.apply_discount())
print(cashRegister.total)

print("------------------")
cashRegister.void_last_transaction()
print(cashRegister.total)
print(cashRegister.items)
