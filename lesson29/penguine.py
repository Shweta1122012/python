class bird:
    def __init__(self):
        print("bird is flying")
    def whoisthis(self):
        print("bird")
    def swim(self):
        print("bird is swimming")
class penguine(bird):
    def __init__(self):
        print("penguine is flying")
        super().__init__()
    def whoisthis(self):
        print("penguine")
    def run(self):
        print("bird is running")
obj = penguine()
obj.whoisthis()
obj.swim()
obj.run()        