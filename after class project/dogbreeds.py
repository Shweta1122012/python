class dog:
    breed1="golden retriever"
    breed2="chihuahua"
    def __init__(self,name,color,breed,age):
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
    def __init__(self,name,color,breed,age):
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
tommy = dog("tommy","brown","golden retriever",6)
lola = dog("lola","white","chihuahua",4)
print(tommy.name,"is a :",tommy.breed1)
print(lola.name,"is a :",lola.breed2)
print(tommy.name, "is",tommy.age,"years old and is",tommy.color)
print(lola.name,"is",lola.age,"years old and is",lola.color)
