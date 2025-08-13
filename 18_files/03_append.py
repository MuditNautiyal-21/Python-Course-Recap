'''
**APPEND**

- Symbol: "a"
- Operation: Opens the file for writing.
- If the file does not exist, it will create a new file.

Question: If Append and Writing both opens the file for writing then what's the point of having two different modes?

Answer: When a file is opened with append mode, data will be added to the end of the file whereas when opened with write mode, it will overwrite the existing data (if any).
'''

# Task: Append to an existing file called John Doe.txt.
# It should add the data about John Doe's hometown

f = open("John Doe.txt", "a")

string = '''
John Doe previously lived in Arizona but now lives in New York!
'''

f.write(string)
f.close()