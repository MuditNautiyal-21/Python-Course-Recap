'''
Command Line Utilities:

One can use Python to create simple command-line utilities.

The "argparse" module makes it easier to handle the command-line arguments.

Whenever we are running a python program. We do python_file_name.py run in the terminal like python main.py.
Now lets say we want to apply some input to main.py through command line.

like: python main.py 4, 9 add.
Ideally it will give an error. 
That is where argparse can help you!
'''

import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")

parser.add_argument("num1", type = float, help="First number")

parser.add_argument("num2", type = float, help="Second number")

parser.add_argument("operation", choices=["add", "sub", "div", "mul"])

args = parser.parse_args()

print(args)

if(args.operation == "add"):
    print(f"The result is {args.num1 + args.num2}")
elif(args.operation == "sub"):
    print(f"The result is {args.num1 - args.num2}")
elif(args.operation == "div"):
    print(f"The result is {args.num1 / args.num2}")
elif(args.operation == "mul"):
    print(f"The result is {args.num1 * args.num2}")
else:
    print("Some Error Occurred.")

# This all lets you do operations from command-line itself.