import numpy as np

a= np.array([
    [1,-2,3],
    [4,5,-6]
]) 

print(a[a<0])   # return negative value of the array
print(a[a>2])   #  value greater than 2
print(a[a%2==0])    # return even value both + , -