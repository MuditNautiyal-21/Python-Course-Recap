'''
**Filter**
filter() function construcs an iterator from elements of an iterable for which a function returns True.

In other words, it filters the iterable based on a condition.
'''

def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False

a = [1, 3, 5, 234, 34, 32, 6543, 23, 2, 5, 6, 7, 43]

new = filter(is_greater_than_9, a)

print(new) # Again this will return a filter object at some memory address

# If we want to see the actual elements of the iterables after the operation, we will need to typecaste it like we did in map:

new = list(filter(is_greater_than_9, a))
print("After Type Casting:\n",new)
print("The length of the original iterable a is: ",len(a))
print("The length of the new iterable after the filter operations: ", len(new))
print("Number of elements filtered out (removed): ", len(a)-len(new))

# We can also have non-numeric objects in the iterables, we just have to come-up with the condition that could give true of false for the iterables and then use the filter object!

# You can also use the lamda function rather than creating a separate function, just know that use the lamda function if its not readable or maintanable!

# Example with lamda:
new = list(filter(lambda x: x>9, a))
print(new)