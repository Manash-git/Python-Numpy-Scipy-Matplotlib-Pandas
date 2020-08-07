import numpy as np

x= np.float32(1)
print(x.dtype)

a= np.array([1,2,3,4], dtype="f")
print(a.dtype)
print(a.astype(int).dtype)

n = np.zeros(5)
print(n)
print(n.dtype)
print(n.astype(int))
print(n.astype(int).dtype)