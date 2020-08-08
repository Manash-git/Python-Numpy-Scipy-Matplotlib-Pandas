import numpy as np

a= np. arange(6)
b= np. arange(5)
c= np. arange(5)

# vstack()
# print(np.vstack((a,b)))
print(np.vstack((b,c)))
print(np.vstack((b,c)).shape)


x= np.array([[1,2],[3,4]])
y= np.array([[5,6]])
print(np.vstack((x,y)))
print(np.vstack((x,y)).shape)

#  hstack()

print(np.hstack((a,b)))
print(np.hstack((c,b)))
# print(np.hstack((x,y)))
# print(np.hstack((x,y.T)))