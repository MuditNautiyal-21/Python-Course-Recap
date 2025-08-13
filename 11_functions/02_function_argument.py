def add(a, b):
    return a + b

c = add(3, 5)
print(c)

# Type of arguments, the one we did was the positional argument case where we have value for each parameter defined in function definition (in the argument bracket ())

# Default Arguments: They have a default value in case of the value not being provided while calling the function...

def add_new(a, b, plus = 0):
    x = a + b + plus
    return x

d = add_new (3,5)
print(d) # The value for plus is not provided while calling, so it will use the default value from the function definition which is 0
d1 = add_new(3,5,2)
print(d1) # In this case, 2 is provided as the value for plus, so it will override the default value of plus...

# Keyword Argument: In this order doesn't matter when calling a function, you call it along naming the exact variable from the function definition...

def student(name, age):
    print(f"Name: {name} & Age: {age}.")

student(age = 27, name = "Dragon") # Observe, we did not provide the values of the arguments in the same order, here order didn't matter because we used the exact same variable in calling as they are in the funciton definition. This avoids any ambiguity...