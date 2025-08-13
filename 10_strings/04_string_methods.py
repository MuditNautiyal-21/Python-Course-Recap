name = "Dragon" # Strings are immutable

# name[0] = "R" # You cannot do this!

# Above will give a runtime error.

# print(name)

a = len(name)
print(a)

print(name.upper()) # Converts every alphabet of the string to upper case

print(name.lower())

s = "DrAgOn"

print(name.lower()) # Converts all the letters of the string to lower case.

# Note: These string methods do not change the actual string in the memory, it creates a temperory variable to show the action on the actual string.

print(s.capitalize()) # Converts the first letter of the string to upper case.

print(s.title()) # Converts first letter of every word in the string to upper case.

# Strip methods
text = " hello world "

print(text.strip()) # Output: "hello world"
print(text.lstrip()) # Output: "hello world "
print(text.rstrip()) # Output: " hello world"

# Find and Replace:

text = "Python is fun"

print(text.find("is")) # Output the index number where it is found, here: 7
print(text.replace("fun", "awesome")) # replaces all the occurances of the given word (if found in the string) with the second word. Here Output: Python is awesome

# Splitting the string:
text = "Apples, Bananas, Pineapples"

print(text.split(","))
print(text.strip().split(","))
print(text.strip().split(", "))

print(", ".join(['Apples', 'Bananas', 'Pineapples']))

# Checking string properties:

text = "Python123"

print(text.isalpha()) # Checks if only alphabet, Output: False here
print(text.isdigit()) # checks if only digits, Output: False
print(text.isalnum()) # Checks if alpha numeric, Output here: True
print(text.isspace()) # Checks if there is any space in the string, Output here: False