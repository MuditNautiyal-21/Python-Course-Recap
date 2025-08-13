'''
Tuples: They are immutable
The difference between the syntax is, the items are enclosed in () rather than [] like in list.

- We use Tuples when we don't want our data to be changed accidently!
'''

a = (3, 2, 22, 13)

print(a)
print(a[2]) # This will show the element at 2nd index
a[3] = 32 # This will generate an error since tuples are immutable


b = (3, ) # In order to create a tuple with just single element, you will have to add a "," comma after the first element.