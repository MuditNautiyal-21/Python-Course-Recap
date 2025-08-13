# Dictionary Comprehension:
# Just like we had comprehension in the lists, we can also have comprehensions in Dictionary as well...

table_of_5 = {i: 5*i for i in range(1, 11)}

print(table_of_5)


'''
Now that we have done the most important part from the Data Structure Section, we now should know when to use which data structure...


** Data Structure: List **
Features: Ordered & Mutable
Best For: Storing sequences, Dynamic data.

** Data Structure: Tuple **
Features: Ordered & Immutable
Best For: Fixed collections, dictionary keys.

** Data Structure: Set **
Features: Unordered & Unique
Best For: Removing duplicates, Set operations.

** Data Structure: Dictionary **
Features: Key : Value pairs.
Best For: Fast lookups, Structured data.
'''