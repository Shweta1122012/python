s1 ={1,2,3,4,5,6}
s2 ={'a','b','c','d','e','f'}
s3 =list(zip(s1,s2))
print(s3)

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,3]
for i,j in zip(l1,l2[ : : -1]):
    print(i,j)

stokes = ['relience','infosys','tcs']
prices = [2435,6574,3985]
new_dict = {stokes:prices for  stokes, prices in zip(stokes,prices)}
print(new_dict)
