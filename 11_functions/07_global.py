# Lets understand the Global keyword for variable: Used to manipulate a global variable...

def sum (a, b):
    c = a + b
    # z = 0 # This will not change the global variable z outside this function.
    # But if we use "global" keyword, it will effect the global variable outside this function:
    global z # This will let the funciton modify the global variable:
    z = 1
    return c

z = 3
print(z)
print(sum(3,12))
print(z)

'''
Excessive use of the "global" is not recommended since it makes the debugging harder!
'''