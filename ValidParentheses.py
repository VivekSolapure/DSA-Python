s="{([)]}"
stack=[]
closetoOpen={")":"(","}":"{","]":"["}

for c in s:
    # print(c)
    if c in closetoOpen:
        if stack and stack[-1] == closetoOpen[c]:
            stack.pop()
        else:
            print(False)
            break
    else:
        stack.append(c)
print(True if not stack else False)