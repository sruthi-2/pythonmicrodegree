# concept of string and list overlap


print(dir(list))
# u can always know about a attribute using help
help(list.append)
mylist = [1, 2, 3, 4, 5, 6]
print(mylist)
mylist.append(10)
print(mylist)
mylist.append("hey hey")
print(mylist)
# remove all items from the list
mylist.clear()
print(mylist)
mylist.append("ash")
mylist.append("mishty")
mylist.append(17)
print(mylist)
'''
The index() method returns the index of the specified element in the list.
The list index() method can take a maximum of three arguments:
element - the element to be searched
start (optional) - start searching from this index
end (optional) - search the element up to this index
he index() method returns the index of the given element in the list.
If the element is not found, a ValueError exception is raised.
Note: The index() method only returns the first occurrence of the matching element.
'''
# find the position
print(mylist.index("mishty"))
# print(mylist.index("mty"))
print(mylist[2])
print(mylist[1:2])
print(mylist[1:3])
print(mylist[:])
print(mylist[:3])
print(mylist[2:])
print(mylist[2:-1])
print(mylist[:-1])

# string
a = "abcdefghijk"
print(a.index('f'))
mylist.append(23)
mylist.append("abc")
mylist.append("abc")
mylist.append("abc")
print(mylist)
print(mylist.index("abc"))
print(mylist[4][1])
# select the item in 4th index,and then 1st index of that 4th index
# same things with dictionaries
student = {
    "name": "ash",
    "age": 17
}
print(student["name"])  # i wana know the name of student
# translation
lang = {
    "water": "pani",
    "morning": "subhah"
}
print(lang["water"])
