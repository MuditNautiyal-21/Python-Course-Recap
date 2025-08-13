# Tuple Methods...

t = (3, 12, 1, 54, 23, 12)

print(t.count(12)) # This will tell the number of times 12 occurred inside the tuple.

print(t.index(12)) # This will tell the index at which 12 exists (It will tell its first occurance).

'''
Why we should use tuples:
- They are faster than the list.
- Since they are hashable, it can be used as dictionaries.
- Change cannot be made - immutable (can safeguard the data from unwanted changes)
'''