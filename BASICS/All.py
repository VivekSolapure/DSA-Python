# a=[1,1,2,3,4]
# a.pop(2)
# print(a)

# from array import array

# i_arr=array("i",[2,4,5,6])
# print(i_arr)
# print("doesn't")
# s = 'First line.\nSecond line.'
# print('First line.\nSecond line.')
# print("""\
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)
# print('Py','thon')

# a="sd"
# b="wqer"
# print(a,b)

# a="python"
# print(a[0:5:6])

# import math
# # print(5 // 2)
# print(-3 // 2)
# print(int(-3/2))
# print(int(3/2))
# print(3//2)
# print("round dowwn ",math.floor(3/2)) # round dowwn 
# print("round up ",math.ceil(3/2)) # round up 
# print("square root ",math.sqrt(4)) # square root
# print("POW",math.pow(2, 3)) # POW

# # Positive Infinity
# pos_inf = float('inf')

# # Negative Infinity
# neg_inf = float('-inf')

# # Example usage
# print(pos_inf)  # Output: inf
# print(neg_inf)  # Output: -inf

# # Arithmetic operations with infinity
# print(5 + pos_inf)   # Output: inf
# print(10 / neg_inf)  # Output: -0.0
# print(10 / pos_inf)  # Output: -0.0
# print(5 - neg_inf)  # Output: inf
# print(math.pow(2,200)< pos_inf)# Output: True

print('################################################ SLICLING ##############################################')
str="Hello, World!"
print(str[0:13])
print(str[0:11])
print(str[0:])
print(str[::2])
print(str[0:13:2])
print(len(str))
print(str[12])
print(str[::-1])

arr=[1,2,3,4,5,6]
print(len(arr))


print("########################################### UNPACKING #######################################")
a,b,c=[1,2,3]
# x,z=[1,2,3]
print(a,b,c)
# print(x,z)

print("###################################### List comprehension #########################################")
ld=["Adf","sfg","g"]
e=[ i for i in ld if 'f' in i  ]
print(e)
print("###################################### Dict comprehension #########################################")
ld=["Adf","sfg","g"]
e={ i:len(i) for i in ld if 'f' in i  }
print(e)
print("###################################### List comprehension #########################################")
ld=["Adf","sfg","g"]
e=[ i for i in ld if 'f' in i  ]
print(e)

print("########################################### 2 D Lists #######################################")
list2D=[[0] *4 for i in range(5)]
print(list2D)
list2D=["Vicky " *4 for i in ld if "f" in i]
print(list2D)
l=[[i for i in range(5)] for i in range(5)]
print(l)


print("########################################### HASHSET #######################################")
hset=set()
hset.add(1)
hset.add(2)
print(hset)
print(1 in hset)
hset.remove(2)
print('REMOVED')
print(hset)
print("LENGTH",len(hset))
print("Bunch of set added using list",set([1,2,3]))
myset={1,2,3}
print(type(myset))


print("########################################### HASHMAP #######################################")
myMap={'a':1,'b':2}
myMap.pop('a')
print(myMap)
mapp={i:2*i for i in range(5)}
print("Dict comprehensin:",mapp)

print("########################################### HEAP #######################################")
import heapq
minHeap=[]
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,1)
heapq.heappush(minHeap,10)
heapq.heappush(minHeap,0)
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,4)
heapq.heappush(minHeap,9)
heapq.heappush(minHeap,5)
print(minHeap)
while len(minHeap):
    print("Popped:",heapq.heappop(minHeap))

# print(minHeap[0])
# for i in range(len(minHeap)):
#     print(minHeap[i])

# maxHeap=[]
# heapq.heappush(maxHeap,-3)
# heapq.heappush(maxHeap,-1)
# heapq.heappush(maxHeap,-2)

# for i in range(len(maxHeap)):
#     print(-1 * maxHeap[i])


print("########################################### FUNCTION #######################################")

def double(arr,val):
    def helper():
        for i in range(len(arr)):
            arr[i]*=2
        
        
        vala=val
        vala*=2
    helper()
    print(arr,val)

nums=[2,6]
val=3
double(nums,val)



print("########################################### CLASS #######################################")

class myClass:
    def __init__(self,nums):
        self.nums=nums
        self.size=len(nums)
    
    def getSize(self):
        return self.size
    
    def doubleGetSize(self):
        return 2* self.getSize()

value1=myClass([1,2,3])
print(value1.getSize())
print(value1.doubleGetSize())
class myClass:
    def __init__(self,make):
        self.make=make
    
    def getSize(self,make):
        return self.make,make

# value1=myClass('gg')
val1=myClass('gg')
print(val1.getSize("vv"))
# print(value1.doubleGetSize())

a=1
a=a+1
a+=1
print()