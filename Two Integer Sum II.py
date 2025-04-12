numbers = [2,3,4]
target = 6
# arr=[]
# length=len(numbers)

# for i in range(1,length-1):
#     if numbers[i]<numbers[i+1] and numbers[i]+numbers[i+1]==target:
#         arr.append(i)
#         arr.append(i+1)
# print(arr)
        
        
################ OPTIMAL ########################

start,end=0, len(numbers)-1

while start<end:
    sum=numbers[start]+numbers[end]
    if sum==target:
        print(start+1,end+1)
        break
    
    if sum<target:  
        start+=1
    elif sum>target:
        end-=1
        