class vehicles:
    def __init__(vehicaltype):
        print("this is a vehical",vehicaltype)
class car(vehicles):
    def __init__(self):
        super().__init__("car")
print(issubclass(car,vehicles))
print(issubclass(car,list))
print(issubclass(car,car))
print(issubclass(car,(list,vehicles)))
