strs= ["neet","code","love","you"]
stringg=''
decoded=[]
storenum=0
start=2
for i in strs:
    stringg+=str(len(i))+"#"+str(i)

# print(stringg)
# i=0
# while i < len(stringg):    
#     j=i
#     while stringg[j] != "#":
#         j+=1
#     lenggth = int(stringg[i:j])
#     decoded.append(stringg[j+1 : j+1+lenggth])
#     i=j+1+lenggth
# print(decoded)

import re
print(stringg)
stringg=re.sub(r"[^a-zA-Z0-9\s]","",stringg)
stringg=re.sub(r"[\d]"," ",stringg)

print(stringg[1:])