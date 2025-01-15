s=set([1,2,3,4,5,5,6])
print(s)#{1, 2, 3, 4, 5, 6}

s.add(8)
print(s)#{1, 2, 3, 4, 5, 6, 8}

x={"a","b","c"}
y={"x","b","y","z"}

print(x|y) #union
print(x&y) #intersection
print(x-y)#difference
print(y-x)

print(x<y)#if x is a subset of y