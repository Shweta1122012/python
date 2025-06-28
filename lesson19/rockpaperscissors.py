import random
options=["rock","paper","scissors"]
userchoice=input("enter your choice rock paper or scissor")
computerchoice=random.choice(options)
print("computer choice =",computerchoice)
print("your choice=",userchoice)
if userchoice==computerchoice:
    print("its a draw")
elif userchoice=="rock" and computerchoice=="scissors":
    print("you won")
elif userchoice=="paper" and computerchoice=="rock":
    print("you won")
elif userchoice=="scissors" and computerchoice=="paper":
    print("you won")    
else:
    print("you lost")    