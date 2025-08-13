def sum(a, b):
    c = a + b # c is restricted to function sum(), can't use it outside the sum() unless defined again, outside... same applies for a and b
    # print(z)
    z = 1 # here it creates a local variable z and is destroyed after this funciton returns.
    return c

def greet():
    z = 32 # local variable to greet()
    print("Hello")

z = 8 # z is a global variable
print(z)
print(sum(4,6))
print(z)

'''
We studied 2 types of variables:
- Global Variable.
- Local Variable.
'''