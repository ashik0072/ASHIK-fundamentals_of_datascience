import numpy as np
sales_data = np.array([10000, 20000, 30000, 40000])
total_sales = sales_data.sum()
first_quarter_sales = sales_data[0]
fourth_quarter_sales = sales_data[3]
percentage_increase = (fourth_quarter_sales - first_quarter_sales)/(first_quarter_sales*100)
print("Total sales for the year : ", total_sales)
print("Percentage increase in sales from the first quarter to the fourth quarter : ",percentage_increase, "%")
