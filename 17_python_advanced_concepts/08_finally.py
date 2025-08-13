# a = int(input("Enter Number 1: "))
# b = int(input("Enter Number 2: "))

# try:
#     c = a/b
#     print(c)
# except Exception as e:
#     print(e)
# finally:
#     print("This is always executed!")

# Finally block is always executed no matter even i ftry completely executed or not!

'''
Now a question may arise, as it came to me earlier, if finally block is executed always, then why do we need finally block when we can do it with just simple print function outside any block of try or except!

The answer to this is hidden in code re-usability.
Lets say we have a function

divide(a,b)
Commenting above block to demonstrate!
'''

def divide(a, b):
    try:
        c = a/b
        print(c)
        return c
    except Exception as e:
        print(e)
        return None
    finally:
        print("This is always executed!")

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

divide(a, b)

# This is the case where it will run and be printed everytime (we are talking about whats inside of finally block.) Since the rules say whenever there are try or except, finally will be executed..

# Now considering the case where it might not execute: Lets say we remove that finally block and just write the simple print statement, it won't get printed:

def divide(a, b):
    try:
        c = a/b
        print(c)
        return c
    except Exception as e:
        print(e)
        return None
    print("This is always executed!")

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

divide(a, b)