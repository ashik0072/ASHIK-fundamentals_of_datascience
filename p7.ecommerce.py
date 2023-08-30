import pandas as pd
data = {'customer_id': [1, 2, 1, 3, 2, 1, 4],
        'order_date': ['2023-07-01', '2023-07-02', '2023-07-02', '2023-07-03', '2023-07-03', '2023-07-04', '2023-07-05'],
        'product_name': ['A', 'B', 'A', 'C', 'B', 'D', 'A'],
        'order_quantity': [3, 2, 4, 1, 2, 3, 2]}
order_data = pd.DataFrame(data)
total_orders_per_customer = order_data['customer_id'].value_counts()
average_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()
print("Total number of orders made by each customer:\n", total_orders_per_customer)
print("\nAverage order quantity for each product:\n",average_quantity_per_product)
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
