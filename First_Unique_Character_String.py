s = "leetcode"
# hashset={}

# for i in s:
#     if i in hashset:
#         hashset[i]=1+hashset.get(i,0)
#     else:
#         hashset[i]=1
        
# min_val=min(hashset.values())

# if min_val>1:
#     print(-1)
# else:
#     key_min=0
#     for key, value in hashset.items():
#         if value==min_val:
#             key_min=key
#             break
#     print(hashset)
#     print(s.index(key_min))


######   NEETCODE
from collections import defaultdict
count= defaultdict(int)
for c in s:
    count[c]+=1
# print(count)

for i,c in enumerate(s):
    if count[c]==1:
        print(i)
print(-1)