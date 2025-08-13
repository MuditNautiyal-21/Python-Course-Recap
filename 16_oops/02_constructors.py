# Constructors: We use constructors in python to initialize our objects

class Employee:
    
    def __init__(self, salary, name, bond):
        self.salary = salary # Created an instance attribute of the name salary and assigned it with salary.
        # This __init__ function is the constructor of the class.
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. The salary is {self.salary} and the bond is for {self.bond} years.")

e1 = Employee(34000, "Dragon", 4)
print(e1.get_salary())

e1.get_info()