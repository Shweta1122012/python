class BMW:
    def milage(self):
        print("BMW has a milage of 15 km/l")
    def speed(self):
        print("BMW can reach a top speed of 240 km/h")
    def color(self):
        print("BMW is available in various colors including black, white, and blue")
class ferrari:
    def milage(self):
        print("Ferrari has a milage of 10 km/l")
    def speed(self):
        print("ferrari can reach a top speed of 350 km/h")
    def color(self):
        print("Ferrari is available in red, yellow, and black")
objBMW = BMW()
objferrari= ferrari()
for country in (objBMW, objferrari):
    country.milage()
    country.speed()
    country.color()  

