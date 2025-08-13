'''
FILE I/O in Python:

- File Input/Output (I/O) refers to reading data from and writing data to files. 
- Python has built-in functions to make this process straightforward.

While working with files, we have few steps involved:
    - Opening a file: One needs to open a file before one can read from it or write to it. This creates connection between your program and the file.
    - Performing Operations: One can then read data from the file or write data to it!
    - Closing the File: Its very important to close the file when the operations are finished. This releases the connection and ensures that any changes one has made are saved.


**READ**
- Symbol: r
- Operation: Opens file for reading. This is the default mode.
- If the file doesn't exist already, it will throw an error.
'''

f = open("file.txt", 'r')

'''
If you are reading from text file we will use 'rt' and if from binary file we use 'rb'.

By defult t in rt is there so thats why we can write only 'r' to read a text file (if its a text file), but we have to specifically mention 'rb' if we are to read from a binary file.
'''

content = f.read()
print(content)

f.close()