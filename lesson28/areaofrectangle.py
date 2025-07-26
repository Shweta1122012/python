class rectangle:
    def __init__(self,lenght,width):
        self.lenght =lenght
        self.width = width
    def area(self):
        return self.lenght * self.width
obj=rectangle(10,20)
print("area of a rectangle is",obj.area())
