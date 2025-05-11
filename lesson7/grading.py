print("enter your 5 subjects marks")
markone=int(input())
marktwo=int(input())
markthree=int(input())
markfour=int(input())
markfive=int(input())

total = markone+marktwo+markthree+markfour+markfive
average = total/5

if average>=91 and average<=100:
    print ("your grade isA1")
elif average>=81 and average<91:
    print("your grade is A2")
elif average>=71 and average<81:
    print("your grade is B1")
elif average>=61 and average<71:
    print("your grade is B2")
elif average>=51 and average<61:
    print("your grade is C1")
elif average>=41 and average<51:
    print("your grade is C2")
elif average>=33 and average<41:
    print("your grade is D")
elif average>=21 and average<33:
    print("your grade is E1")
elif average>=0 and average<21:
    print("your grade is E2")
else:
    print("invalid input")
