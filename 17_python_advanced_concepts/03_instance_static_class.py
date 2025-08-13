class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    # Instance Method
    def print_info(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
    
    # Static Method : Decorator
    @staticmethod
    def sum(a, b):
        return a+b
    
    # Class Methods : Decorator
    @classmethod
    def print_company(cls):
        print(cls.company)
    
    # Class Methods : Decorator
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        print(cls.company)

e1 = Employee("Jack", 35000)
e2 = Employee("Jill", 35000)

print(Employee.company)
# print(Employee.name) # This will throw an error.

e1.print_info()
e2.print_info()
print(e2.sum(5, 23)) # This will give an error because it will convert that to another call which will have e2 as parameter i.e. sum is being called with e2 as parameter.

# To resolve this, we can write @staticmethod : It is a method that does not require self.

e1.print_company()
e2.print_company()

e1.change_company("Asus")
e2.change_company("Acer") 
# The last company assigned in this case will actually change the name of the company inside the class (for variable company)
print(Employee.company)