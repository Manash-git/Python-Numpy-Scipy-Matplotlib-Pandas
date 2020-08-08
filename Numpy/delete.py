import numpy as np

a= np.arange(1,11)

print(a)
print(np.delete(a,2))

x= np.array([
    [1,2],
    [3,4],
    [5,6]
    ])

print(x)

print(np.delete(x,1))
print(np.delete(x,[2,5]))