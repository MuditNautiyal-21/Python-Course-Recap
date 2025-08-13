# while True:
#     a = int(input("Enter Number 1: "))
#     b = int(input("Enter Number 2: "))
#     print(f"The sum is {a + b}")

'''
So we saw that the above piece of code run endlessly if the user enters integers but if someone puts lets say characters or strings as input the program ends up throwing error and ends there!

To deal with this situation - in case when the user even by mistake enters a wrong input, in that case, rather than the program end, it should throw a customized error and the next set of input or cycle should continue...

To have it happen, we will use try and except block (commenting the above code set!)
'''

# while True:
#     try:
#         a = int(input("Enter Number 1: "))
#         b = int(input("Enter Number 2: "))
#         print(f"The sum is {a + b}")
#     except:
#         print("Some Error Occurred!!!")

# So you see now, in case of a wrong input, the program says "Some Error Occurred!!!" and continues the cycle leaving that wrong input behind.

# We can also post, exception as e....lets see it in action:

# while True:
#     try:
#         a = int(input("Enter Number 1: "))
#         b = int(input("Enter Number 2: "))
#         print(f"The sum is {a + b}")
#     except Exception as e:
#         print("Some Error Occurred!!!", e)

# except Exception as e will save the error thrown by the compiler into e and if you want, as I did, you can also print e and e as many functions attached to it, you can try if you want to just e.function_name it, like I did in string functions section.

######################################

# Now, we can handle some known errors for example ZeroDivisionError like this
# while True:
#     try:
#         a = int(input("Enter Number 1: "))
#         b = int(input("Enter Number 2: "))
#         print(f"The sum is {a / b}")
    
#     except ValueError:
#         print("Please don't perform bad typecasts...")

#     except ZeroDivisionError:
#         print("Hey don't divide by 0.")

#     except Exception as e:
#         print("Some Error Occurred!!!", e)

# We can also raise an error:

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

if b == 0:
    raise ValueError("Please don't divide by 0. Its not defined.")
print(f"The sum is {a / b}")