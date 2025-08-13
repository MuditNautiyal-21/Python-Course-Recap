'''
Dictionaries:

- Created with {}.
- Come with key : value pairs.
- Allows fast lookup.

Note: Whenever you are creating a dictionary, you can have any data type as key or as value but the key you are using should always be HASHABLE. i.e., Python should be able to hash that particular data type internally.

* Hashables: Strings, Integers, Tuples
* Not hashables: Lists
'''

marks = {"Dragon":34, "Jack":45, "Lily": 94}

print(marks, type(marks))

print(marks["Lily"]) # To see Lily's marks dictionary_name[key]

marks["Dragon"] = 91 # This changes the marks for Dragon i.e. changes the value for the key - Dragon
print(marks)