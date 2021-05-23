mylist = [12, 32, 34, 2, 4]
mydictinry = {"one": 32, "two": 322, "three": 32, "four": 4}


def avg(n):
    if type(n) == dict:
        print("its a dictionary")
        avg = sum(n.values()) / len(n)
        print("average is ", avg)
    else:
        print("its a list")
        avg = sum(mylist) / len(mylist)
        print("average is ", avg)


avg(mylist)
avg(mydictinry)
'''
The isinstance() function returns True if the specified object is of the specified type, otherwise False.
If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.

isinstance(object, type)
so the code can be changed as
'''


def avgs(n):
    if isinstance(n, dict):
        print("its a dictionary")
        avg = sum(n.values()) / len(n)
        print("average is ", avg)
    else:
        print("its a list")
        avg = sum(mylist) / len(mylist)
        print("average is ", avg)


avgs(mylist)
avgs(mydictinry)
'''
if else
'''

if 3 > 1:
    print("3 greater")
elif 3 == 1:
    print("equal")
else:
    print("3 smaller")
