def sum (a, b):
    '''This will sum 2 numbers.'''
    c = a + b
    return c


print(sum.__doc__) # This will print the comment inside the function called which contains the information about the function. You can also hover over the function and it will show the description.

# Let's see an example of writing a detailed docstring:

def add(a, b):
    """
    Returns the sum of 2 numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the 2 numbers.
    """
    
    return a + b

print(add.__doc__)