import numpy as np

arr=np.array([[1,2],[3,4],[5,6]])
print(arr.ndim)#dimension of array

print(arr.itemsize)#byte Size of the array
print(arr.dtype)


mat=np.array([[1,2],[3,4],[5,6]],dtype=np.float32)
print(mat.itemsize)
print(mat.dtype)
print(mat)

print(mat.size)
print(mat.shape)

print("reshape: ",mat.reshape(2,3))
CompMat=np.array([[1,2],[3,4],[5,6]],dtype=complex)
print(CompMat)
print("raveld: ",mat.ravel())
print("sum:",mat.sum())
print("min: ",mat.min())
print("max: ",mat.max())
print("sum of cols: ",mat.sum(axis=0))
print("sum of rows: ",mat.sum(axis=1))
print("square roots: ",np.sqrt(mat))

zeroMat=np.zeros((3,2))
print(zeroMat)
oneMat=np.ones((2,3))
print(oneMat)

ls=np.linspace(1,5,10)
print(ls)

# 2
# 8
# int64
# 4
# float32
# [[1. 2.]
#  [3. 4.]
#  [5. 6.]]
# 6
# (3, 2)
# reshape:  [[1. 2. 3.]
#  [4. 5. 6.]]
# [[1.+0.j 2.+0.j]
#  [3.+0.j 4.+0.j]
#  [5.+0.j 6.+0.j]]
# raveld:  [1. 2. 3. 4. 5. 6.]
# sum: 21.0
# min:  1.0
# max:  6.0
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]
# [[1. 1. 1.]
#  [1. 1. 1.]]
# [1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222
#  3.66666667 4.11111111 4.55555556 5.        ]

