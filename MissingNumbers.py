nums =[1,0,3]
res=len(nums)
missing=''

# for i in range(len(nums)):
#     if 0 not in nums:
#         missing=0
#         break
#     elif len(nums) not in nums:
#         missing=len(nums)
#         break
#     elif nums[i]+1 not in nums and nums[i]!=len(nums):
#         missing=nums[i]+1
# print(missing)

# solution2
for i in range(len(nums)):
    print(i,nums[i])
    res+=i-nums[i]
    print(res)
print(res)