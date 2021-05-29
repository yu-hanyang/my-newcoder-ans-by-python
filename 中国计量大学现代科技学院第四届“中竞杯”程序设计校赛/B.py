n=int(input())
s=input()
a=[]
if s[0]=='B':
    a.append(0)
    a.append(0)

t=0
for i,j in enumerate(s):
    if j=='A' and t==0:
        a.append(i)
        t=1-t
    elif j=='B' and t==1:
        a.append(i-1)
        t=1-t
    if i==n-1 and t==1:
        a.append(i)
if s[-1]=='B':
    a.append(n-1)
    a.append(n-1)
maxl=0
for i in range(3,len(a)):
    maxl=max(maxl,a[i]-a[i-3]+1)

print(maxl)

