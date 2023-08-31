import pandas as pd
import numpy as np

a = pd.read_csv('CSV_FILES/FOOTBALL.csv')
print(a)
print("Player with most number of goals: ")
c = a.sort_values(by='no_of_goals', ascending=False)
print(c.head())

print("High paid players")
s = a.sort_values(by='salary', ascending=False)
print(s.head())

m = np.mean(a['age'])
print(m)

x = a[a['age'] > m]
print(x)
