numbers = [1,2,3,4,5]
numbers2 =[6,7,8,9]
result = map(lambda x,y:x+y, numbers,numbers2)
print(list(result))
def sq(n):
    return n*n
nums=[1,2,3,4,5,6,7,8]
result2 =  list(map(sq,nums))
print(result2)