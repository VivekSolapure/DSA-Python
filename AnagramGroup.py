from collections import defaultdict


strs = ["act","pots","tops","cat","stop","hat"]
hashMap=defaultdict(str)
counts,counta={},{}

for i in strs:
    count=[]*26
    for c in i:
        count[ord(c)-ord('a')]+=1
    hashMap[tuple(count)].append(i)