# String Formatting

template = "Dear {}, You are awesome. Take this ${} bag."

a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c2 = 300

s1 = template.format(a,a1)
print(s1)

print(f"{a}, You are awesome, take this ${a1} bag with you.")

# ord() & chr()
print(ord('A')) # Gives the ASCII value of A or any letter given to the function.
print(chr(65)) # Gives back the character from the ASCII value given to the function.