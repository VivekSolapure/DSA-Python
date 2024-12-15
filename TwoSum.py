nums=[1,0,2,3,5,6]
target=5
# prevSet={}# 4:0,3:1,2:2
# def TwoSum():
#     for i,n  in enumerate (nums):
#         diff=target-n
#         if(diff in prevSet):
#             return [prevSet[diff],i]
#         prevSet[n]=i            
# print(TwoSum())
# print(prevSet)
    
    
start=0
end=len(nums)-1
for i in range(len(nums)):
    sum=nums[start]+nums[end]
    if sum<target:
        start+=1
    elif sum>target:
        end-=1
    else:
        print([start,end])
        break
    