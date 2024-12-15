arr=['a','d','w','e','r','t','y','u','i']

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)
