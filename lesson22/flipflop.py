def palindrome(r):
    e =len(r)-1
    s= 0
    while s<e:
        if r[s]!=r[e]:
            return False
        s +=1
        e -=1
    return True
r = (1,2,3,4,4,3,2,1)
if palindrome(r):
    print("it is a flip flop")
else:
    print("it is not a flip flop")
    