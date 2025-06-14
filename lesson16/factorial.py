def factorial(x):
    '''using this function to calculate the factorial of a number'''
    if x== 0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("the factorial of 0 -",factorial(0))
print("the factorial of 1 -",factorial(1))
print("the factorial of 4 -",factorial(4))
print("the factorial of 9 -",factorial(9))
print("the factorial of 23 -",factorial(23))