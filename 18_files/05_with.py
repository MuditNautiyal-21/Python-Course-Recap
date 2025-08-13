'''
**WITH**

- This is another method to read file with.

- Speciality: Sometimes people either forget to close the file or don't like to close the file every now and then! Although its not an error but its not a good practice also. "With" is the solution to this.

- Once the "with" statement block is over, the file is closed automatically!
'''

# Earlier method:
f = open("file.txt", "r")
content = f.read()
print(content)
f.close()

# New Method: With

with open("file.txt", "r") as f:
    content = f.read()
    print(content)