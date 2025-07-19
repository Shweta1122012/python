test_dict ={"codingal": 3, "is": 2, "best": 2, "for": 2, "coding": 1}
print("The orignal dictionary is:",test_dict)
k=int(input("enter the frequency to check"))
res=0
for key in test_dict:
    if test_dict[key]==k:
        res+=1
print ("yhe number of times the given number is reapeting is:",res)