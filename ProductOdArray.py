
'''
Time complexity:
    The time complexity of this code is O(n^2) because there are nested loops that iterate over 
    the input array `nums`. The outer loop runs `n` times, where `n` is the length of the input array, 
    and the inner loop also runs `n` times for each iteration of the outer loop. 
    Therefore, the total number of iterations is n * n = n^2.

Space complexity:
    The space complexity of this code is O(n) because we are creating an additional array `arr` 
    to store the products of all elements except the current element in the input array. 
    The size of this array is equal to the length of the input array `nums`, 
    so the space complexity is O(n).
'''

nums = [-1,0,1,2,3]
product=1
arr=[]
for i in range(len(nums)):
    for j in range(len(nums)):
        if j==i:
            continue
        else:
            product*=nums[j]
    arr.append(product)
    product=1
print(arr)