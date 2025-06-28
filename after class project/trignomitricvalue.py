import math
number = int(input("enter a number?"))
print("1.sin")
print("2.cos")
print("3.tan")
choice=(input("choose which trignometric value you want to calculate"))

if choice=="sin":
    print("the sin value is=",math.sin(number))
elif choice=="cos":
    print("the cos value is=",math.cos(number))
elif choice=="tan":
    print("the tan value is=",math.tan(number))
else:
    print("invalid input")