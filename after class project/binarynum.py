decimal =int(input("enter a decimal number:"))
binary=""
while decimal >0:
    remainder=decimal %2
    for i in range(1):
        binary=str(remainder)+binary
    decimal=decimal//2
print (binary)
