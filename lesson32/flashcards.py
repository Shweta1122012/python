class flashcards:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+">"+self.meaning
flash =[]
print("welcome to flashcards app")
while True:
    word = input("enter the word")
    meaning = input("enter the meaning")
    flash.append(flashcards(word,meaning))
    option = int(input("if you want to add another flashcard press0 else press1"))
    if option:
        break
print("your flashcards are")
for i in flash:
    print("-",i)


    

    