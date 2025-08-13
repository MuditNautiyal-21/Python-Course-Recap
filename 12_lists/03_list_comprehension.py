# List Comprehension:

# Create a list containing the table of 5...

a = 5
table = []

for i in range(1, 11):
    table.append(a*i)

print(table)

# This is great, but this method is long, there is another method called "List Comprehension", that can ease out this for you...

# This is how you will do with list comprehension:
table = [a*i for i in range(1, 11)]

print(table)