import numpy as np
import matplotlib.pyplot as plt
x=np.array([1995,1998,2001,2004,2007,2010,2013,2016,2019,2022])
y=np.array([55,72,48,77,78,68,97,42,100,97])
n=np.size(x)
mx=np.mean(x)
my=np.mean(y)
mxy=np.sum(x*y)-n*mx*my
mxx=np.sum(x*x)-n*mx*mx
b=mxy/mxx
a=my-b*mx
ypred=a+b*x
plt.scatter(x,y)
plt.plot(x,ypred)
plt.show()
