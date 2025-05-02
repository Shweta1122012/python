amount=int(input("enter the the amount"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("number of 100 notes are:",note1)
print("number of 50 notes are:",note2)
print("number of 10 notes are:",note3)