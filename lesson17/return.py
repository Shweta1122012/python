no1=int(input("enter the number"))
no2=int(input("enter the number"))
no3=int(input("enter the number"))
def greater(no1,no2,no3):
    if no1>no2 and no1>no3:
        return no1
    elif no2>no1 and no2>no3:
        return no2
    else:
        return no3
print(greater(no1,no2,no3))