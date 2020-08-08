import numpy as np

a= np.array([
    [10,20],
    [30,40]
])

b= np.array([
    [1,2],
    [3,4]
])

# print(a*b)
# print(a.dot(b))     # this is matrix multiplication

x= np.matrix("1 2; 3 4")
y= np.matrix([
    [10,20],
    [30,40]
])
print(x)
# print(y)
# print(y.T)
print(np.linalg.inv(x))     # inverse  a matrix
# print(x*y)