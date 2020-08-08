import numpy as np

a= np.arange(11)
print(a)
print(np.append(a,20))

x= np.array([
    [1,2],
    [3,4]
])
print(x)
print(np.append(x,[[10,20]],axis=0))
# print(np.append(x,[[10,20]],axis=1))
print(np.append(x,[[10],[20]],axis=1))