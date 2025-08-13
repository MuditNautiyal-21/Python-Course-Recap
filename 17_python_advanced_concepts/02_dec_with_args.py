# We are here to see how decorators work with arguments!

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

# Above is also an example of nested functions inside nested function - its like or can be called "Double Nested".

@repeat(7)
def say_hello(a):
    print(f"Hello {a}!")

'''
In this case the decorator function would look like this...It replaces say_hello function with this:

def decorator(say_hello):
    def wrapper("John"):
        for i in range(7):
            say_hello("John")
'''

say_hello("John")

'''
Decorators are a key feature of python that enables code reusability and cleaner function modification.

Decorators are commonly used for:

- Logging: Recording when a function is called.
- Timing: Measuring how long a function takes to execute.
- Authentication & Authorization: Checking if the user has permission to access a function.
- Caching: Storing the reuslts of a function call so that subsequent calls with same arguments can be returned quickly.
- Rate Limiting: Controlling how often a function can be called.
- Input validation: Checking if the arguments to a function meet a certain criteria.
- Instrumentation: Adding monitoring and profiling to functions.
'''