nums = [1,2,2,3,3]
# unique=[]
count={}
k=2
# for i in range(len(nums)):
#     # print(nums[i],nums[count])
#     if len(nums)==1:
#         unique.append(nums[i])
#         break
         
#     if nums[i] in nums[i+1:] and nums[i] not in unique and len(unique)<k:
#         unique.append(nums[i])

# count={}
# freq=[[] for i in range(len(nums)+1)]

# for i in nums:
#     count[i]=1+count.get(i,0)

# for n,c in count.items():
#     freq[c].append(n)

# print(freq)
# res=[]

# for i in range(len(freq)-1, 0, -1):
#     for n in freq[i]:
#         print(n)
#         res.append(n)
        
# print(res[:k])
    
for i in range(len(nums)):
    count[nums[i]]=1+count.get(nums[i],0)
# print(count)

freq=[[] for i in range(len(nums))]
arr=[]
for i,a in count.items():
    freq[a].append(i)
print(freq)
for a in range (len(freq)-1,0,-1):
    
    for i in freq[a]:
        if len(arr)==k:
            break
        arr.append(i)
print(arr)

            
    