# Set Methods...

s = {34, 23, 1, 3, 22}

print(s)

s.add(32) # This will add 32 to the set

print(s)

s.add(322) # It will add 322 to the set but can be at any position
print(s)

s.remove(32) # will remove 32 from the set.
print(s)

# s.remove(434234) # when the number is not present in the set, this will throw an error...Therefore we can use discard() set method, it will keep it silent
s.discard(434234)
print(s)

s.pop() # This will remove a random element from the set!
print(s)