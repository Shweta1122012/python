x = input ("enter a charecter")

if len(x)>1:
    print("\nwrong input!")
else:
    if x>='a' and x<='z':
        print("is an alphabet")
    elif x>='A' and x<='Z':
        print ("is an alphabet")
    else:
        print("is not an alphabet")