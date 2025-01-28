import numpy as np

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

for i in arr.flatten():
    print(i)

for i in np.nditer(arr,order='C'):
    print(i)

for i in np.nditer(arr,order='F',flags=['external_loop']):
    print(i)


for x in np.nditer(arr,op_flags=['readwrite']):
    x[...]=x*x
print(arr)

b=np.arange(3,15,4).reshape(3,1)
for x,y in np.nditer([arr,b]):
    print(x,y)

1
2
3
4
5
6
7
8
9

1
2
3
4
5
6
7
8
9

[1 4 7]
[2 5 8]
[3 6 9]

[[ 1  4  9]
 [16 25 36]
 [49 64 81]]

1 3
4 3
9 3
16 7
25 7
36 7
49 11
64 11
81 11