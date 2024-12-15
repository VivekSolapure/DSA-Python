arr=[5,6,1,0,4]

for i in range(len(arr)-1):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            temp=arr[i+1]
            arr[i+1]=arr[i]
            arr[i]=temp
print(arr)