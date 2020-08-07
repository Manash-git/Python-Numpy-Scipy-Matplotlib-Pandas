import numpy as np

a= np.arange(1,6)
print(a)
print(a+2)
print(a*2)
print(a**2)
print(a//2)

b= np.array([10,20,30,40,50])
print(a+b)

d2 = np.array([[1,2],[3,4]])
print(d2)
print(d2*3)
d21= np.array([
    [5,6],
    [7,8]
])
print(d2+d21)
print(np.add(d2,d21))