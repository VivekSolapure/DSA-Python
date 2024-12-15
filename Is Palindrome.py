import re

s = "Was it a car or a cat I saw?"
s1=s.replace(" ","").lower()[::-1]
s2=s.replace(" ","").lower()
if re.sub(r"[^a-zA-Z0-9\s]", "", s1)== re.sub(r"[^a-zA-Z0-9\s]", "", s2):
    print(True)
