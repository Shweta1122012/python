class parrot:
    species="birds"
    def __init__ (self,name,age):
        self.name=name
        self.age=age
kiki=parrot("kiki",10)
koko=parrot("koko",12)
print("kiki is a :",kiki.species)
print("koko is a :",koko.species)
print(kiki.name,"is",kiki.age,"years old")
print(koko.name,"is",koko.age,"years old")

