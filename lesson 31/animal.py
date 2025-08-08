from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk and run")
class fish(animal):
    def move(self):
        print("I can swim")
class bird(animal):
    def move(self):
        print("I can fly")
class dog(animal):
    def move(self):
        print("I can bark")
a=human()
a.move()
b=fish()
b.move()
c=bird()
c.move()
d=dog()
d.move()
