import pandas as pd
import matplotlib.pyplot as plt
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'Sales_Values': [10000, 6900, 29000, 3400, 20000, 19000, 28000, 25000, 9000, 7000, 20000, 18000]}
dataframe_data = pd.DataFrame(data)
print(dataframe_data)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(dataframe_data['Month'], dataframe_data['Sales_Values'])
plt.subplot(1, 2, 2)
plt.bar(dataframe_data['Month'], dataframe_data['Sales_Values'])
plt.tight_layout()
plt.show()
