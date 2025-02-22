# list comprehension
num=[1,2,3,4,5,6]
even=[]
for i in num:
    if i%2==0:
        even.append(i)
print(even)

even2=[i for i in num if i%2==0]
print(even2)

sqr=[i*i for i in num]
print(sqr)

s=set([7,8,8,9,10,11,12])
print(s)
s2={i for i in s if i%2==0}
s3={i for i in num if i%2==0}
print(s2)
print(s3)
