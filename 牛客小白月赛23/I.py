d={}
s=input()
for i in range(len(s)):
    if s[i] in d:
        d[s[i]]=max(d[s[i]],s[i:])
    else:d[s[i]]=s[i:]
a=sorted(d.items(),key=lambda x:x[1])
print(a[-1][-1])