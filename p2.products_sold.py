import pandas as pd
import numpy as np
data={"car_toy":[100,90,60],"bike_toy":[90,40,50],"rc_car":[20,25,50]}
product=pd.DataFrame(data)
product.index=['jan','feb','mar']
print(product)
arr=product.to_numpy()
arr.shape=(3,3)
mean=np.mean(arr,axis=(1))
allprod=sum(mean)
print(arr)
print(mean)
print(allprod)

