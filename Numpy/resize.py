import numpy as np
# resize will fill the the extra space by repeating data

a= np.arange(5)
print(a)
print(np.resize(a,(5,2)))   # It will retunrn a new array
print(a)
b = a.resize((5,2))
print( b)