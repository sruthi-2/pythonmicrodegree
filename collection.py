'''
python is a hll
it is compiled b4 interpreted
it is not a interpreted language

'''
'''
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is ordered(from Python version 3.7)and changeable. No duplicate members.
'''

'''
Lists are used to store multiple items in a single variable.
List items are indexed, the first item has index [0], the second item has index [1] etc.
'''
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
list1 = ["abc", 34, True, 40, "male"]
print(list1)
list1.pop(3)  #many fns exist
print(list1)
'''
Tuples are used to store multiple items in a single variable
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
tuple1 = ("abc", 34, True, 40, "male")
'''
Sets are used to store multiple items in a single variable.A set is a collection which is both unordered and unindexed.

Sets are written with curly brackets.Set items are unordered, unchangeable, and do not allow duplicate values.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
Once a set is created, you cannot change its items, but you can add new items.
Duplicate values will be ignored
'''
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
set1 = {"abc", 34, True, 40, "male"}
'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict.keys())  #show just keys
print(thisdict.values())  #show just values
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
'''
Python in Keyword
The in keyword has two purposes:

The in keyword is used to check if a value is present in a sequence (list, range, string etc.).

The in keyword is also used to iterate through a sequence in a for loop
'''

print("test")
list1=[3,2,5,7,3,6]
list1.pop(3)
print(list1)
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
  print("yes")
dictionary = {"geek":10, "for":45, "geeks": 90}
print("geek" in dictionary) #returns true

'''
Among Tuples and List — when to use which
Use a tuple when you know what information goes in the container that it is. For example, when you want to store a person’s credentials for your website.

person = (‘ABC’, ’admin’, ’12345')

But when you want to store similar elements, like in an array in C++, you should use a list.

groceries = [‘bread’, ’butter’, ’cheese’] 
'''
a ={}   #set
a['a']= 1
a['b']=[2, 3, 4]
print(a)

print(29 % 4)
list1 = [1, 3, 5, 2, 4, 6, 2]

list1.remove(2)

print(sum(list1))
