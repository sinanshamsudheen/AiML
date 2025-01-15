
import time
import multiprocessing

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

if __name__ == "__main__":
    t1=multiprocessing.Process(target=calc_square,args=(arr,))
    t2=multiprocessing.Process(target=calc_cube,args=(arr,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
#  o/p,
#  calculating square: 
# calculating cube: 
# square: 1
# cube: 1
# square: 4
# cube: 8
# square: 9
# cube: 27
# square: 16
# cube: 64
# square: 25
# cube: 125


# //////////////////////////////////////////

import time
import multiprocessing

square_result=[]
def calc_square(numbers):
    global square_result
    print("calculating square: ")
    for num in numbers:
        time.sleep(5)
        square_result.append(num*num)

arr=[1,2,3,4,5]

if __name__ == "__main__":
    t1=multiprocessing.Process(target=calc_square,args=(arr,))
    t1.start()
    t1.join()
    print('result:',square_result)
# O/P,
# calculating square: 
# result: []

    




# calculating square: 
# calculating cube:
# square: 1cube: 1

# square: 4
# cube: 8
# square:cube:  927

# cube:square:  6416

# cube: 125
# square: 25
