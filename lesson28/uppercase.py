class IOSstring:
    def __init__ (self):
        self.string=""
    def get_string(self):
        self.string = input("Enter a string: ")
    def print_string(self):
        print(self.string.upper())
IOS=IOSstring()
IOS.get_string()
IOS.print_string()