for i in range(5):
    print(i,end=" ")
print()

for line in open("sample.txt"):
    print(line)

for element in [7,8,9]:
    print(element)

for element in (7,8,9):
    print(element)

for key in {"one":1,"two":2}:
    print(key)

for value in {"one":1,"two":2}.values():
    print(value)

for char in "976":
    print(char)

arr=[4,5,6,7]
itr=iter(arr)
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))

itr2=reversed(arr)
print(next(itr2))
print(next(itr2))
print(next(itr2))

0 1 2 3 4 

the world is beautiful lie

everyone loves food

monkeys have tails

7
8
9

7
8
9

one
two

1
2

9
7
6

<list_iterator object at 0x0000026DF54FBFD0>
4
5
6

7
6
5