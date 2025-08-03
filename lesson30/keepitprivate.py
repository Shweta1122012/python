class myclass:
    __privatevar =24
    def __privatemethod(self):
        print("i am in private method")
    def hi(self):
        print("private variable",myclass.__privatevar)
obj = myclass()
obj.hi()
obj.__privatemethod()
