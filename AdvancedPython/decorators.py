import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + "ms.")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result = []
    for num in numbers:
        result.append(num*num)
    return result

@time_it
def counter():
    count=0
    for i in range(1000):
        count+=1
    return count
numb=[1,2,3,4,5]
print(calc_square(numb))
print(counter())

