import pandas as pd
import numpy as np
data={  "maths":[100,90,60,80],"science":[90,40,50,60],"social":[20,33,57,68],"english":[90,40,55,66]}
student=pd.DataFrame(data)
student.index=['ashik','sooriya','ayush', 'obed']
print(student)
arr=student.to_numpy()
print(arr)
mean=np.mean(arr,axis=(1))
print(mean)
print(np.max(mean))
print("maths has high average")
arr.shape=(4,4)
print(arr)
