x=int(input("enter the speed of the first cyclysit:  "))
y=int(input("enter the speed of second cyclysit:"))
z=int(input("enter the speed of third cyclysit: "))

average =x+y+z/3
if x<average:
    print("first cyclysit is slower than the average and the diffrence is",average-x)
if y<average:
    print("second cyclistis slower than the average and the difference is",average-y)
if z<average:
    print("third cyclist is slower than the average and the differnce is",average-z)
