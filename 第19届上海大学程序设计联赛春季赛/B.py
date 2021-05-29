s=input()
d={}
l=len(s)
t=0
for i,j in enumerate(s,1):
    d[i]=j
    if i>=l//2+1:
        if j!=d[l+1-i]:
            break
else:t=1



f=l//2+1

for _ in range(int(input())):
    x,c=input().split()
    x=int(x)
    if l&1 and x==f:
        print('Yes')
    elif d[x]!=c and t==1:
        t=1-t
        d[x]=c
        print('No')
    elif d[x]!=c and t==0:
        d[x]=c


        for i in range(1,f):
            if d[i]!=d[l+1-i]:
                break
        else:t=1
        if t==1:
            print('Yes')
        else:print('No')
    elif d[x]==c:
        if t==1:
            print('Yes')
        else:
            print('No')

