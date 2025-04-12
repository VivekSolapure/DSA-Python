s = "loveleetcode"
hashset={}

for i in s:
    if i in hashset:
        hashset[i]=1+hashset.get(i,0)
    else:
        hashset[i]=1
        
max_val=max(hashset.values())
print(hashset)
key_max=0
for key, value in hashset.items():
    if value==max_val:
        key_max=key
print(key_max,max(hashset.values()))