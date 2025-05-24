base = int(input("enter the base number:"))
exponent=int(input("enter the exponent"))
result=1
for i in range (exponent):
    result=result*base
print(base,"to the power of",exponent,"is",result)
