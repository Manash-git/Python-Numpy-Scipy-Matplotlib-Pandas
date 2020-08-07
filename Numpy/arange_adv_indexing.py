import numpy as np

#  numpy.arange(start, stop, step, dtype)

# print(np.arange(3))
# print(np.arange(3.0))
# print(np.arange(3,10))
# print(np.arange(5,30,2))
# print(np.arange(4,30,2))

a= np.arange(1,11)
# print(a)
# make index for retrieve value
index= np.array([1,4,5])
# print(a[index])     # way- 1
# print(a[[1,4,5]])   # way- 2

# also can get repleadly acces of index
# print(a[[1,4,4,5,2,3,4,4,9]])

# how to access 2d array

arr2d= np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# print(arr2d)
print(arr2d[[0],[1]])       # [ [row] , [col] ]
print(arr2d[[0,1],[1,2]])   # [ [row,row], [col,col] ]

print(arr2d[ [0,1,2,], [2,1,0]]) 
