test_dict = {"codingal": 2, "is":2,"the":2,"best":2,"for":2,"coding":1}
print("The orignal dictionary is:",test_dict)
k=2
res=0
for key in test_dict:
    if test_dict[key]==k:
        res+=1
print("the number of time two is reapeating is:",res)