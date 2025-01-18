import numpy as np
n=[6,7,8]
print(n[0:2]) #[6,7]

a=np.array([6,7,8])
print(a[0:2]) #[6 7]

b=np.array([[6,7,8],
            [1,2,3],
            [9,3,2]])
print(b)
print(b[1,2]) #3
print(b[0:2,1]) #[7 2]

print(b[-1,0:2])
print(b[:,1:3])
for a in b.flat: #flatten
    print(a,end=",")

for a in b.ravel():
    print(a)

c=np.arange(6,15).reshape(3,3)
print(c)

v=np.vstack((b,c))
print("v stacked: ",v)
h=np.hstack((b,c))
print("h stacked: ",h)

resSplit=np.vsplit(v,3)
print("split 1\n",resSplit[0])
print("split 2\n",resSplit[1])
print("split 3\n",resSplit[2])
print(np.hsplit(b,3))

m= b > 4
print(m)

print(c[m])
c[m]=-1
print(c)

# [6, 7]
# [6 7]
# [[6 7 8]
#  [1 2 3]
#  [9 3 2]]

# 3

# [7 2]
# [9 3]
# [[7 8]
#  [2 3]
#  [3 2]]

# 6,7,8,1,2,3,9,3,2,

# 6
# 7
# 8
# 1
# 2
# 3
# 9
# 3
# 2

# [[ 6  7  8]
#  [ 9 10 11]
#  [12 13 14]]

# v stacked:  
# [[ 6  7  8]
#  [ 1  2  3]
#  [ 9  3  2]
#  [ 6  7  8]
#  [ 9 10 11]
#  [12 13 14]]

# h stacked: 
#  [[ 6  7  8  6  7  8]
#  [ 1  2  3  9 10 11]
#  [ 9  3  2 12 13 14]]

# split 1
#  [[6 7 8]
#  [1 2 3]]
# split 2
#  [[9 3 2]
#  [6 7 8]]
# split 3
#  [[ 9 10 11]
#  [12 13 14]]

# [array([[6],
#        [1],
#        [9]]), array([[7],
#        [2],
#        [3]]), array([[8],
#        [3],
#        [2]])]

# [[ True  True  True]
#  [False False False]
#  [ True False False]]

# [ 6  7  8 12]

# [[-1 -1 -1]
#  [ 9 10 11]
#  [-1 13 14]]