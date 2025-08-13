'''
Dunder Methods: Also called Magic methods

- Dunder Method is a Double Underscore Method.
- Allow us to define how objects interact with built-in python operators, functions, and language constructs.
'''

class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    # Magic Method: __str__
    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    
    # Magic Method: __repr__
    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary}"
    
    # Magic Method: __len__
    def __len__(self):
        return len(self.name)


e = Employee("Jack", 45000)
print(e.name, e.salary)
print(str(e)) # Meant for the user to see...
print(repr(e)) # Meant for the developer to see...

print(len(e)) # this will throw an error saying the object type Employee has no len(). There we have to implement our own version of len...yes the Magic Method...