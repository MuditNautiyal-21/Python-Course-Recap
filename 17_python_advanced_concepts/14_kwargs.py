'''
**Kwargs: (Keyword Arguments)

**kwargs collects any extra keyword arguments passed to a function into a dictionary.

- Again, kwargs is the conventional name, but one can use any valid variable name preceded by two asterisks, example: **data, **keyargs


** Difference between *args and **kwargs **:
- *args save the extra positional arguments in a tuple.
- ** kwargs save the extra keyword arguments in a dictionary.

**Note**: *args saves the positional arguments and **kwargs save the keyword arguments.
'''

def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to marks() function here
    for item in kwargs.keys():
        print(f"The marks that {item} got is {kwargs[item]}")

marks(Shubham = 34, Vikrant = 54, John = 34, Marrie = 90)

