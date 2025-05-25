string=input("enter your word:")
char=input("enter your charactor")
i=0
count =0
while i <len(string):
    if string [i]==char:
        count=count+1
    i=i+1
print("the number of times the charector has occured is",count)
