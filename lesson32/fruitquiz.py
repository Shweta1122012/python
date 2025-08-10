import random
class fruitquiz:
    def __init__(self):
        self.fruits={
            'apple':'red',
            'banana':'yellow',
            'grape':'purple',
            'orange':'orange',
            'kiwi':'brown',
            'watermelon':'green'
        }
    def quiz(self):
        while True:
            fruit,color = random.choice(list(self.fruits.items()))
            print("what is the color of",fruit)
            answer = input()
            if answer.lower() == color:
                print("correct")    
            else:
                print("wrong answer")
            option= int(input("if you want to continue press 0 else press 1"))
            if option:
                break
print("welcome to fruit quiz")
obj = fruitquiz()
obj.quiz()
