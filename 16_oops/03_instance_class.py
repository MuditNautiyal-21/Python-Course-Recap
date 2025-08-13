# Instance & Class Attributes

'''
- Instance Attributes: Specific to an Instance.

- Class Attributes:  Specific to a Class.
'''

class Employee:
    company = "Asus" # This is a class attribute

    def __init__(self, salary, name, bond, company):
        self.salary = salary 
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. The salary is {self.salary} and the bond is for {self.bond} years.")
        
e1 = Employee(3500, "Dragon", 3, "Tesla")
print(e1.company) # This will always pront the instance attribute whenever present
print(Employee.company) # This will always print the class attribute.

# Object Introspection:
print(dir(e1))