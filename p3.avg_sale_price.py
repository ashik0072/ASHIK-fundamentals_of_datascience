import pandas as pd
import numpy as np
house_data = pd.read_csv("C://Users//ASHIK C SABU//Desktop//housing.csv")
print(house_data)
b = house_data[house_data['total_bedrooms'] > 4]
print(b)
sales_prices = b['median_house_value']
print(list(sales_prices))
avg_sales_price = np.mean(list(sales_prices))
print(f"The Average Sale Price of house with more than four bedrooms in the neighborhood : {avg_sales_price}")
