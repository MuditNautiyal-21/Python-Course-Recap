'''
OS and Shutil Module: Built-In Python module

os module: Provides functions for interacting with the operating system, such as working with directories and files.

shutil module: It offers higher-level file operations.
'''

import os

a = os.listdir("dir") # gets all the files and sub-directories inside a directory stated in listdir()

print(a)

# lets check current working directory

print("Current Working Directory",os.getcwd())

print(os.path.exists("file.txt")) # this helps check whether a file exists or not! Returns True or False.

# We can also remove files with os.remove()

# os.remove("sample.txt")

# If you want to remove directory:
os.rmdir("dir/sub")