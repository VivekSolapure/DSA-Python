nums = [-2,1,-3,4,-1,2,1,-5,4]
nums= set(nums)
nums=sorted(nums)
nums= list(nums)
arr=[]
currentSum=0
# print(len(nums))
for i in range(len(nums)-1,-1,-1):
    currentSum+=nums[i]
    
    if nums[i]<0:
        break
print(currentSum)