'''
**Reduce**
reduce() function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value.

- reduce is not a built-in function.
- It must be imported from the functools module.
'''
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]

def sum(a, b):
    return a+b

c = reduce(sum, numbers)

print(c)

'''
So this is how the operation went:
step 1-> add first 2 elements: 1 + 2 = 3
new list = numbers = [3, 3, 4, 5, 6]

step 2-> add the first 2 elements of new list: 3 + 3 = 6
new list = numbers - [6, 4, 5, 6]

step 3 -> Repeat the above steps until there is only one element left in the iterable:

[6, 4, 5, 6]
[10, 5, 6]
[15, 6]
[21]

so 21 will be the answer....
'''