
try:
    num1 = int(input("enter your age"))
    if num1<0 or num1>120 or num1==0 or num1 not in int:
        raise ValueError
    
    else:
        if num1%2==0:
            print("your age is in even number")
        else:
            print("your age is in odd number")
except ValueError :
    print("invalid input")






    




