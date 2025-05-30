rows =int(input("enter the number of rows:"))
for i in range(1,rows+1,2):
    spaces =(rows-i)//2
    print(" " * spaces,end="")
    for j in range(1,i+1):
        print(j,end="")
        
    print()
for i in range(rows-2,0,-2):
    spaces =(rows-i)//2
    print(" " * spaces,end="")
    for j in range(1,i+1):
        print(j,end="")
    print() 
