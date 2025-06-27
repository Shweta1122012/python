valid = False
while not valid:
    try:
        number= int(input("enter a number:"))
        while number%2 == 0:
            print("bye")
        
        valid = True
    except ValueError:
        print("invalid input")