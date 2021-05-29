s=input()
out=0
for i,j in enumerate(s):
    if i==0 and j>='a' and j<='z':
        out+=1
    elif i==0:
        continue
    elif j<='z' and j>='a' and s[i-1]<='Z' and s[i-1]>='A':
        out+=1
    elif j<='Z' and j>='A' and s[i-1]<='z' and s[i-1]>='a':
        out+=1
print(out)