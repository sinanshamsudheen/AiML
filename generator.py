def remote_control_next():
    yield "HBO"
    yield "CNN"
    yield "NATGEO"

itr=remote_control_next()
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr))

for c in remote_control_next():
    print(c)


def fib():
    a,b=0,1
    while True:
        yield a
        a=b
        b=a+b
for f in fib():
    if f > 50:
        break
    print(f)

# Advantages over iterators: no need to init iter or next functions, doesnt require to raise StopIteration

# <generator object remote_control_next at 0x0000022E89F092D0>
# HBO
# CNN
# NATGEO
# HBO
# CNN
# NATGEO
# 0
# 1
# 2
# 4
# 8
# 16
# 32
