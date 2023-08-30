import pandas as pd
data = {'products': ['eclairs', '5star', 'milkyway', 'milkybar', 'dairymilk', 'chupachups', 'rings', 'candyman', 'kachamango', 'mangobite'],
        'order_quantity': [50, 80, 44, 19, 48, 34, 89, 97, 78, 69]}
sales = pd.DataFrame(data)
print(sales)
sorting_sales_price = sales.sort_values(by='order_quantity', ascending=False)
print(sorting_sales_price)
top_products = sorting_sales_price.head(5)
print("\n\nThe Top Selling Product of the Past Month are \n\n",top_products)
