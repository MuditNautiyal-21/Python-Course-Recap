# Data Strutures: It starts with lists
'''
- List
- Tuples
- Sets
- Dictionaries

Here we are going to start with Lists
'''

marks = [54, 23, 64, 93, 32] # List - Enclosed in square brackets, separated by "," (comma)

# List is ordered, mutable (changeable) collections of items. It can contain different data types.

mixed = [43, "Hello", False, 4.2]

print(marks)
print(mixed)

# To access the element of the list, we can do it by providing the index inside [], similar to what we did in strings...

print(marks[0]) # first element of list marks
print(mixed[1]) # Second element of list mixed.

# We can also do slicing in list:
print(marks[2:4])

# Lists have order, if one calls the list, it will come in the same order as it was created in.

# print(mixed[4]) # This will generate an error since there is no element at index 4!


# Since list is mutable, we can change the original list, even at a particular index

mixed[1] = "Hello World!" # Earlier it was just Hello at mixed[1]

print(mixed)