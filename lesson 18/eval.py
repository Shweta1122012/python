try:
    num1 ,  num2 =eval(input("enter teo numbers spreated by a comma:"))
    result = num1/num2
    print("the result is:",result)
except ZeroDivisionError:
    print("you can not put zero for division")
except SyntaxError:
    print("put a comma in between the numbers, like this 4,5")
except :
    print("wrong or invalid input")
else:
    print("the operation was suscessful")
finally:
    print("this will print no matter what")
    
