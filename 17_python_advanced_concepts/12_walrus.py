'''
Walrus Operator (:=):

- Symbol: :=
- Introduced in: Python 3.8
- Operator Type: Assignement Expression Operator.
- Allows us to assign a value to a variable within an expression.
- Helps making the code more concise and in some cases, more efficient by avoiding repeated calculations or function calls.
- Name Walrus Operator comes from operator's resemblence to the eyes and tusk of a walrus.
'''

def very_slow_func():
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    return 70

a = very_slow_func()
if(a > 10):
    print(a)
else:
    print("Its not greater than 10")

# This is what usual scenario would look like. Lets have a look how would we do it with walrus operator and make the program more efficient.

print("With Walrus Operator:::")

if((a:=very_slow_func()) > 10):
    print(a)
else:
    print("Its not greater than 10")

# Lets see a more simpler case:
print("Simpler Case: ==>")
while(data:=input("Enter the value: ")):
    print(data)
    if data == "q":
        break

# In single line we are checking whether the data is blank or not and also we are collecting the data inside the variable.
# If q is entered, while loop will break and if there is nothing entered just a blank input and pressed enter, walrus operator will end the loop/program.