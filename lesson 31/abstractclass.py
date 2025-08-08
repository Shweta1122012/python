from abc import ABC, abstractmethod
class absclass(ABC):
    def print(self,x):
        print("passed value",x)
    @abstractmethod
    def task(self):
        print("i am inside the abstract method")
class test(absclass):
    def task(self):
        print("hi")
testobj= test()
testobj.print(100)
testobj.task()