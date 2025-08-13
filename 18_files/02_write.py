'''
**WRITE**

- Symbol: 'w'
- Operation: Opens file for writing.
- If the files exists, its contents will be overwritten.
- If the file does not exist, a new file will be created.
'''

# Task: Write to a file called John Doe.txt.
# It should contain the data about John Doe.

f = open("John Doe.txt", "w")

string = '''
John Doe is a 28 year old guy.
He lives in New York and he works in python.
His favorite hobby is to juggle with python.
'''

f.write(string)
f.close()