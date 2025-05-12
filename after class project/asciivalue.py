char=input ("Enter a character:")
if len(char)==1:
    ascii_value=ord(char)
    print("The ASCII value of is",ascii_value)
else:
    print("invalid input")
    print("please only enter a single character")
