class pairelement:
    def twosum(self,nums,target):
        lookup={}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target- num], i)
            lookup[num] = i
sum = int(input("enter the number you wanna search:"))
print("index1=%d, index2=%d"%pairelement().twosum((10,20,30,40,50),sum))

