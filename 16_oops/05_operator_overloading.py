# Operator Overloading

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}.")
    
    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))

p1 = Point(3, 2)
p2 = Point(6, 3)

p = p1.sum(p2) # Returns a new point which is a sum of p1 and p2

p.print_point()


# Now this is how we can do Operator Overloading....

p = p1 + p2 # we overloaded the + operator by writing the __add__ function
p.print_point()