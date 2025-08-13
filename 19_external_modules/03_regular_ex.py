'''
Regular Expressions:

- Regular expressions (also called regex) are powerful tools for pattern matching in strings.

- Python's "re" module provides support for regex.
'''

import re
text = "The quick brown fox jumps over the lazy dog."

# Search for the pattern:

match = re.search("brown", text)
print(match)

if match:
    print("Match Found!")
    print("Start Index:", match.start())
    print("Ending Index:", match.end())

# Find all occurrences of a pattern:
matches = re.findall("the", text, re.IGNORECASE)
print("Matches:", matches)

# To replaces the occurrences of a pattern:
new_text = re.sub("fox", "cat", text)
print("New text:", new_text)

# To learn patterns more: regexr.com is the website one should visit.