'''
We can also read a file line by line.

Lets see it in action:
'''

f = open("file.txt", "r")

for line in f:
    print(line)

f.close()