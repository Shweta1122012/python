class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print("name",self.name)
        print("id",self.id)
class employee(person):
    def __init__(self,name,id,salary,post):
        self.salary =salary
        self.post = post
        person.__init__(self,name,id)
obj=employee("John", 101, 50000, "Manager")
obj.display()