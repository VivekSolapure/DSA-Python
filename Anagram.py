s="vivek";
a="keviv";
counts,counta={},{}
for i in range(len(s)):
    print(counts)
    counts[s[i]]=1+counts.get(s[i],0)
    counta[a[i]]=1+counta.get(a[i],0)

# print(counts)
# print(counta)
if(counts==counta):
    print("anagram")