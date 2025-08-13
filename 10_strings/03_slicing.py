name = "Dragon"

print(name[0:2]) # Goes from 0 to 1 (2-1)

print(name[2:-1]) # This will take from 3rd letter to the second last letter, as in our case it will take from a to o

new_name = "Dragon0123456789"
print(new_name[0:10])

# print(new_name[0:10:n]) # Skip n-1 characters till 10th index
print(new_name[0:10:1]) # skip 0 characters till 10th index
print(new_name[0:10:2]) # Skip 1 character till 10th index

print(new_name[:4]) # Replace the first empty number with 0 # name[0:4]
print(new_name[1:]) # Replace the second empty number with length # name[1:15]