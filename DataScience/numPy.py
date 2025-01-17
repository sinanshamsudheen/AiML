import numpy as np
import timeit
import sys

l=range(1000)
print(sys.getsizeof(5)*len(l))

array=np.arange(1000)
print(array.size*array.itemsize)

size=10000
l1=range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)

s=timeit.default_timer()
res=[(x+y) for x,y in zip(l1,l2)]
e=timeit.default_timer()
print("lists took",(e-s)*1000,"ms")

s2=timeit.default_timer()
res=a1+a2
e2=timeit.default_timer()
print("arrays took",(e2-s2)*1000,"ms")

n1=np.array([1,2,3])
n2=np.array([4,5,6])
print(n1+n2)
print(n1-n2)
print(n1/n2)
print(n1*n2)

# 28000
# 8000
# lists took 1.0910000000876607 ms
# arrays took 0.15499999972234946 ms
# [5 7 9]
# [-3 -3 -3]
# [0.25 0.4  0.5 ]
# [ 4 10 18]
