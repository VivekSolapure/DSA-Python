#creation:-

graph={i:[] for i in range(1,5)}
print(graph)

#taking input for values of graph
links=[]
for i in range(5):
    links_line=list(map(int, input().split()))
    links.append(links_line)
#adding elements
for i in range(5):
    if links[i]:
        graph[i+1]=links[i]
print(graph)