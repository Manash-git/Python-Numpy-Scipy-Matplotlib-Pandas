import numpy as np
#  syntax:= reshape (array, shape, order)

a= np.arange(10)
print(a.shape)
print(np.reshape(a,(5,2)))
print(np.reshape(a,(5,2), order="F"))
print(np.reshape(a,(2,5)))
print(np.reshape(a,(2,5)).shape)