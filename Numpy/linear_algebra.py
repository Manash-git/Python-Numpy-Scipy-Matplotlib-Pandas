import numpy as np

y= np.matrix([
    [10,20],
    [30,40]
])

print(np.linalg.inv(y))

print(np.linalg.matrix_power(y,0))
print(np.linalg.matrix_power(y,1))
print(np.linalg.matrix_power(y,2))
print(y*y)