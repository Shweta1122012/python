print ("chose your ride")
print("1.car")
print("2,bike")
choice=int(input("enter your ride choice:"))
if choice==1:
    print("whta type of car")
    print("1xuv")
    print("2sportscar")
    choice1=int(input("enter which type of car:"))
    if choice1==1:
        print ("u have chosen xuv")
    else:
        print("u have chosen sports car")
elif choice==2:
    print ("what type of bike")
    print("1.scooty")
    print("2.scooter")
    choice2=int(input("enter wiche type of car"))
    if choice2==1:
        print("you have choosen scooty")
    else:
        print ("you have choosen scooter")
else:
    print("wrong input")
