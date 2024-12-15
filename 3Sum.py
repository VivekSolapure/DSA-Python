nums = [-1,0,1,2,-1,-4]
nums.sort()
print(nums)
start,end=1,len(nums)-1
target=3
res=[]


# for i in range(len(nums)):
#     if nums[i]==nums[i-1]:
#         continue
#     start, end = i + 1, len(nums) - 1
#     while start<end:
#         if start > i + 1 and nums[start] == nums[start - 1]:
#             start += 1
#             continue
#         if end < len(nums) - 1 and nums[end] == nums[end + 1]:
#             end -= 1
#             continue
#         sum=nums[i]+nums[start]+nums[end]
#         lis=[nums[i],nums[start],nums[end]]
#         print("sum,lis",sum,lis)
#         if sum==target:
#             res.append(list(map(int,lis)))
#             start += 1
#             end -= 1
#         elif sum<target:
#             start+=1
#         elif sum>target:
#             end-=1
# print(res)    
        
for i in range(len(nums)):
    # print(sum)
    while start<end:
        sum=nums[i]+nums[start]+nums[end]
        # print(nums[i],nums[start],nums[end],sum)
        if sum<target:
            start+=1
        elif sum>target:
            end-=1
        else:
            print([i,start,end])
            res.append(i)
            res.append(start)
            res.append(end)
            break
    if sum==target:
        break
    start,end=0,len(nums)-1
    sums=0
    
print(res)
    
    

