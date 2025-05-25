num=int(input("enter your number:"))
num_str=str(num)
if len(num_str)>=4:
    mid1_index=len(num_str)//2-1
    mid2_index=len(num_str)//2
    mid1=int(num_str[mid1_index])
    mid2=int(num_str[mid2_index])
    product=mid1*mid2
    print("the middle digits are",mid1,mid2)
    print("the product is",product)
else:
    ("enter number should be greater than 4 digits!")
