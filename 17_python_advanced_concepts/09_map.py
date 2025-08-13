'''
Map - Filter - Reduce

- These are high-order functions in python(and in many other programming languages) that operate on iterables like list, tuples etc.

- Provide a concise and functional way to perform common operations on sequences of data without using explicit loops.

- While they are more central to python's functional programming style in earlier versions, list comprehensions and generator expressions often provide a more readable alternative in modern Python.

**MAP**
map() function applies a given function to each item of an iterable and returns an iterator that yields the results.
'''

numbers = [1, 2, 3, 45, 4, 21]

def square(x):
    return x*x

new = map(square, numbers)

print(new) # this will give the map object at some memory address.

# For us to be able to see the elements after the operation, we would need to type caste it:
new = list(map(square, numbers))
print("After type casting:\n", new)