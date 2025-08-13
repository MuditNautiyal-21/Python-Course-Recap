# Inheritance:

class Animal: # Parent Class: SuperClass
    location = "America"
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Speaking now.....")

class Dog(Animal): # Child Class of Class Animal & This is how inheritance is done in python...
    def speak(self):
        super().speak() # This will also call the method/function from the parent class...
        print("Woof!")

a = Animal("Dog")
a.speak()

d = Dog("Bruno")
d.speak()
print(d.location)


'''
super(): Inside a child class, super() lets you call methods from the parent class.

- highly useful when there is a need to extend the parent class's behaviour instead of completely replacing it.

- Especially needed when initializing parent class's part of child object...
'''