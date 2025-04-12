s="vivek";
a="kevivv";
counts,counta={},{}
for i in range(len(s)):
    # print(counts)
    if s[i] in counts: 
        counts[s[i]]=1+counts.get(s[i],0)
    else:
        counts[s[i]]=1
        
for i in range(len(a)):
    # print(counts)
    if a[i] in counta: 
        counta[a[i]]=1+counta.get(a[i],0)
    else:
        counta[a[i]]=1

print(counts)
print(counta)
if(counts==counta):
    print("anagram")