print("right angle triangle pattern made by stars")
n=int(input("enter number of rows:"))
for i in range(n):
    for j in range (i+1):
        print("*",end="")
    print()