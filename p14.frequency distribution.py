import pandas as pd
import numpy as np
import collections
data = {
    'customer_ID': [12, 23, 34, 45, 56, 67, 78, 89],
    'customer_age': [30, 25, 28, 32, 22, 20, 30, 25]
}
df = pd.DataFrame(data)
age = df['customer_age']
age_frequency = collections.Counter(age)
print(age_frequency)
