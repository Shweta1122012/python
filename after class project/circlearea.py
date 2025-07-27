radius_user = int(input("Enter the radius of the circle: "))
class circle:
    def __init__(self,radius,pi=3.14):
        self.radius =radius
        self.pi = pi
    def area(self):
        return self.pi *(self.radius**2)
    def circumferance(self):
        return 2 * self.pi * self.radius
obj=circle(radius_user)
print("area of a circle is",obj.area())
print("circumference of the circle is", obj.circumferance())