import numpy as np

a= np.arange(1,11)
# print(a)

# Systax: insert(arr, before_which_index, value, axis = None)

# print(np.insert(a,2,45))
# print(np.insert(a,8,25.26))
# print(np.insert(a,(4,9),1021))


x= np.array([[1,2],[3,4]])
print(x)
print(np.insert(x,1,245))

# axis = 0 row wise
# axis = 1 col wise
print(np.insert(x,1,245,axis=0)) 
print(np.insert(x,1,245,axis=1))

print(np.insert(x,1,[10,20],axis=0))