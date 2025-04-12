nums = [0,1,0,3,12]
# insert_pos = 0
        
# # Move all non-zero elements to the front
# for num in nums:
#     if num != 0:
#         print(nums[insert_pos])
#         nums[insert_pos] = num
#         print(nums)
#         insert_pos += 1
        
# # Fill the rest of the list with zeros
# while insert_pos < len(nums):
#     nums[insert_pos] = 0
#     insert_pos += 1
    
    
l=0

for r in range(len(nums)):
    if nums[r]:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
print(nums)
        
        