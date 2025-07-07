square_input = int(input("enter a number to find the square and find out if it is even or odd:"))
def square_(start, end):
    for i in range(start, end+1):
        square_num = i**2
        if square_num%2==0:
            print("the square of",i,"is",square_num,"and it is even")
        else:
            print("the square of",i,"is",square_num,"and it is odd")
square_(square_input, square_input)

    