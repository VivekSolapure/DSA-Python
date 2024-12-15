heights=[2,2,2]
print("len",len(heights))
start,end=0,len(heights)-1
res=0
for i in range(len(heights)):
    container=abs(start-end) * min(heights[start],heights[end])

    if (heights[start]<heights[end]):
        print("<")
        start+=1
    elif (heights[start]>heights[end]):
        print(">")
        end-=1
    elif (heights[start]==heights[end]):
        print("=")
        end-=1
    print(container)
    res=max(res,container)
print("res",res)
