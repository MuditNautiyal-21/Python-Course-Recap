'''
Args & Kwargs:
These are special syntaxes in python function definitions that allow you to pass a variable number of arguments to a function.

They are used when you don't know in advance how many arguments a function might need to accept!

**Args**: (Positional Arguments)
*args collects any extra positional arguments passed to a function into a tuple.

- The name args is just a convention, you could use any valid varianle name preceded by a single asterisk, for example *var, *values etc.
'''

def sum(a, b):
    return a+b

print(sum(342, 2))

# But what if I want to give more numbers to sum() function. It will give an error here in our current scenario.

# We will use *args and modify the function a bit:
def new_sum(*args):
    # args will be a tuple of all the values passed to sum (here sum is our function)
    total = 0
    for item in args:
        total += item
    return total

print(new_sum(342, 2, 7))
print(new_sum(342, 2, 7, 9))