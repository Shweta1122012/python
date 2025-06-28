import random
playing = True
number= str(random.randint(10,30))
while playing:
    guess =input("i will chosse a number betwen 10 to 30, try and guess it -")
    if guess==number:
        print("you won",number)
        break
    else: 
        print("you are wrong try again")

