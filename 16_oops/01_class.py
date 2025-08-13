'''
Classes: Encapsulates what represents the real world scenario.

OOPs - Object Oriented Programing in python uses classes.

Why bother with OOP?

- Organization: Your code becomes more structered and easy to navigate.
- Reusability: You can use the same object of classes multiple times.
- Easier Debugging: If something goes wrong, it is easier to pin-point the problem section.
- Real-World Modeling: OOP allows one to represent the real-world things and their relationship in a more natural way.

** Four-Pillars of OOP:**
1. Abstraction: You can write bundles of codes without actually making the user understand what the code is doing.

2. Encapsulation: It is bundling the data/code/methods together within a class. It protects data from being accidentally changed or misused outside the class.

3. Inheritance: It is same as to how children inherit some qualities from parents, similarly in classes there are some children classes which inherit from their parent class or classes (sometimes inheritance is done from multiple classes).

4. Polymorphism: Poly means many and morph means forms. This means that objects of same class can respond in a different way to a same request. Same method name, different behavior.
'''

# Lets take an example of any regular application form that contains name, age, electives, father's name etc...

# Object: A specific instance created from a template called class. E.G. Form which contains the data for John Doe...

class Employee:
    company = "HP"

    def get_salary(self):
        return 34000 # consider all employees are getting salary of 34000
e = Employee() # An object of class Employee is created here.
print(e.get_salary()) # Employee's get salary method is called here.

e2 = Employee()
print(e2.get_salary())

# self references to the object which is been used to call the members/methods of the class. Self basically refers to the object of the class that is created and is used to call a particular function of that class.

# It is mandatory to give self as the first argument to the method that is defined within the class...

print(e2.company)