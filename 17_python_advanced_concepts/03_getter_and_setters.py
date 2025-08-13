'''
Getters & Setters:

These are the extension of class: OOPs concept!
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @property
    def first_name(self):
        fn = self.name.split(" ")
        # print(fn)
        return fn[0]
    
    @first_name.setter
    def first_name(self, first):
        fn = self.name.split(" ")
        new_name = f"{first} {fn[1]}"
        self.name = new_name

e = Employee("Jack Smith", 35000)
# e.projects = 6
# print(e.projects)

# print(e.first_name())
# e.set_first_name("John")
# print(e.name)

'''
It would be awesome if we have some other and catchy syntax or code follow...

We can do this: (below)

Explanation: We can build a property decorator
'''

print(e.first_name)
e.first_name = "John"
print(e.name)