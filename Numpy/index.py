# Below 2D array
arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]

print(arr)

# now create it to numpy array
import numpy as np

n_arr= np.array(arr)
print("2D-np-array=> \n",n_arr)

# basic indexing 
print(n_arr[0][3])
print(n_arr[1][3])
print(n_arr[2][3])

# Below 3D array

ar3d=  [
        [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]
        ],
        [
            [13,14,15,16],
            [17,18,19,20],
            [21,22,23,24]
        ]
]

n_ar3d= np.array(ar3d)
print("3D-np-array=> \n",n_ar3d)

# indexing to 3d array

# syantax a [layer],[row],[col]

print(n_ar3d[1][0][3])
print(n_ar3d[1][2][3])
print(n_ar3d[1][2][0])