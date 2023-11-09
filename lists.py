# Lists
# Lists are used to store multiple items in a single variable.
# Lists are indexed and ordered.
# Lists allow duplicate values.
# Lists are mutable.
# Can store different data types in a single list.
# Lists are written with square brackets.


marks = [95,96,97,98,99,99,100,"shine"]
marks.append(101)
print(marks)

print(marks[0:3])
marks.insert(2,99.5)
print(marks.count(99))