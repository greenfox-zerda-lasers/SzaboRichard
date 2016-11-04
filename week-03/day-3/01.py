# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area

class Circle(object):
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return self.pi * (4 *self.radius)
    def get_area(self):
        return self.pi * self.radius

aKor = Circle(10)
print("Ez a korom terulete: ", aKor.get_area())
