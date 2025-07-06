numbers=[1,9,4,5,3,8,2,7,0,6]
print("orignal list is",numbers)
sum=0
for  i in numbers:
    sum+=i
average = sum/len(numbers)
print ("the sum",sum)
print("the average",average)
numbers.sort()
print("the sorted",numbers)
print ("the smallest element is",numbers[0])
print ("the largest",numbers[-1])