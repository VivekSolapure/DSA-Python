nums = [0,3,7,2,5,8,4,6,0,1]
    
arr=[]
for i in nums:
    if i-1 not in nums:
        length=1
        while i+ length in nums:
             length+=1
        arr.append(length)
print(max(arr))