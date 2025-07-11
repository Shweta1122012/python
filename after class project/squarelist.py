
def square_filter(start, end):
    squares =[]
    even = []
    odd = []

    for num in range(start, end+1):
        sq=num**2
        squares.append(sq)
        if sq % 2 == 0:
            even.append(sq)
        else:
            odd.append(sq)
    print("Squares:", squares)
    print("Even Squares:", even)
    print("Odd Squares:", odd)
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
square_filter(start, end)
    
    