# Basics of Functions in Python

a = 4
b = 2
c = 1

average = (a + b+ c)/3

print(average)

a1 = 6
b1 = 3
c1 = 9

average1 = (a1 + b1 + c1)/3

print(average1)

# You can't keep going for declaring the variables and assigning values and calculating average again and again for every new scenario! There comes the FUNCTIONS in python that generalizes this for you...

def average(a, b, c):
    avg = (a + b + c)/3
    print(avg)

print("Calling through average function...")

average(1 ,2, 3)
average(3,9,3)

# Lets say if you want to write the average value from the function to another variable say like:
o1 = average(1,2,6)
print("The first iteration to save the value of average from function: ", o1)

# and if you now will try to print the value of o1, it won't work since the function returned the value of average and not returned it in order to be carried forward as per convinience!

# We will have to use return statement like this:

def avg(a, b, c):
    d = (a + b + c)/3
    return d # this lets the function return the value to be used as per the requirement further, like to be saved in another variable

o1 = avg(1,2,6)

print("The second iteration to save the value of average from function: ", o1)

# Basics for function end here...