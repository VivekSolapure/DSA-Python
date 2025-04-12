str='adfwe'
rev=''.join(reversed(str))
print(rev)
revv=''

for i in range(len(str)-1,-1,-1):
    revv+=str[i]