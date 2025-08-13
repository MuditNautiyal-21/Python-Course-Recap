'''
Lets say you want to use both!

The combined case of args and kwargs is a special case.

**Condition to USE:**
- In the function definition, inside the brackets
    - *args will be defined before **kwargs (* args, **kwargs - the order should be same)
    - There can never be a case where **kwargs are defined first and *args later.
'''

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 4, 5, jack = 34, john =56, jill = 49,marie = 90)