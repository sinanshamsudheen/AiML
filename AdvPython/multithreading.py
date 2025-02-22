import time
import threading

def calc_square(numbers):
    print("calculating square: ")
    for num in numbers:
        time.sleep(0.2)
        print('square:',num*num)


def calc_cube(numbers):
    print("calculating cube: ")
    for num in numbers:
        time.sleep(0.2)
        print('cube:',num*num*num)

arr=[1,2,3,4,5]

t1=threading.Thread(target=calc_square,args=(arr,))
t2=threading.Thread(target=calc_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

# calculating square: 
# calculating cube:
# square: 1cube: 1

# square: 4
# cube: 8
# square:cube:  927

# cube:square:  6416

# cube: 125
# square: 25
