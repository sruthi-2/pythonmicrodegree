
marks = [12, 34, 23, 4, 3]
# list
grade = {"A": 40, "B": 53, "c": 32}
print(grade.keys())  #show just keys
print(grade.values())  #show just values
averg = sum(grade.values()) / len(grade)
print(averg)
print(len(grade)) #length of dictionary

student = {
  "name": "Ash",
   "age": 19,
  "passed": True,
  "marks": [29,30,78]
}
print(type(student))  #type
