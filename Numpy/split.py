import numpy as np

a = np.arange(1,10)
print(np.split(a,3))

print()
x= np.arange(1,13)
print(x.reshape(2,6))
# print(x.reshape(2,6))
x= np.arange(1,13).reshape(2,6)
print(np.hsplit(x,3))
y= np.arange(1,13).reshape(6,2)
print(y)
print(np.vsplit(y,2))
