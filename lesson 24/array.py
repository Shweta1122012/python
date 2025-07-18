import array as ar
array1 = ar.array("i",[1,2,3,4,3,6,7,5,4,6,2,2,4,5,4,2,7,8,9,4])
print("yhe orignal array is",array1)
array1.reverse()
print("the reversed array is",array1)
print("the number of times 4 is reapeating is",array1.count(4))