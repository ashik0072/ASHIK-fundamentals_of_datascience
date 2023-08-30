import numpy as np
item_prices = []
item_size = int(input("Enter the size of the item:"))
for i in range(0, item_size):
    a = int(input("Enter the item price:"))
    item_prices.append(a)
quantities = []
quantities_size = int(input("Enter the size for quantities:"))
for i in range(0, quantities_size):
    b = int(input("Enter the quantities data:"))
    quantities.append(b)
discount_rate = int(input("Enter the discount rate:"))
tax_rate = int(input("Enter the tax_rate:"))
subtotal = sum(item_price * quantity for item_price,quantity in zip(item_prices, quantities))
discount_amount = subtotal * (discount_rate / 100)
total_after_discount = subtotal - discount_amount
tax_amount = total_after_discount * (tax_rate / 100)
final_total_cost = total_after_discount + tax_amount
print("Total cost for the customer's purchase: {:.2f}".format(final_total_cost))
