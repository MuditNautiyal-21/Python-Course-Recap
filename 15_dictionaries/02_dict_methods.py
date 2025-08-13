marks = {"Dragon":34, "Jack":45, "Lily": 94}

print(marks.keys()) # .keys() gets you the keys inside a dictionary.

print(marks.values()) # .values() hets you the values inside a dictionary.

# Top pop a particular key from the dictionary, we can use .pop()

# .clear() empties the dictionary

marks.pop("Dragon")
print(marks)

marks.clear()
print(marks)