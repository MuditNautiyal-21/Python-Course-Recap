'''
Decorators:

- Allow us to modify and enhance the existing function.
'''
# Decorator is a function that takes a function and creates a new function inside it (wrapper()). Then it returns a new function.
def decorator(func):
    def wrapper(): # wrapper function
        print("I am about to execute a function...")
        func()
        print("I have executed this function...")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()

# Now, we can modify this function

# f = decorator(say_hello)
# f()
# The above syntax is good but there is another alternative to this: We can @decorator above the say_hello function
'''
f will look something like this (func will be replaced by actual action that is being taken by the function that is passed into the decorator function):

def f():
    print("I am about to execute a function...")
    print("Hello")
    print("I have executed this function...")

'''