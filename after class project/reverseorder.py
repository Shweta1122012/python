number =int(input("enter the number:"))
reverse_number=0
while number>0:
    rem=number%10
    reverse_number=reverse_number*10+rem
    number=number//10
    print ("the reverse number of your enterd number is",reverse_number)
