class vehical:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
class bus(vehical):
    pass
schoolbus = bus("schoolt ABC", 75,9)
print("details of the vehical",schoolbus.name,"maxsppeed is",schoolbus.maxspeed,"and mileage is",schoolbus.mileage)
