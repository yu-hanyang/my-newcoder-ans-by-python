n,m=map(int,input().split())
ys=[0]*(n+1)
d={}
t=1
for i in range(m):
    s=list(map(int,input().split()))
    if s[0]==1:
        t+=1
        for j in range(s[1],s[2]+1):
            if j in d:
                d[j][t]=1
            else:
                d[j]=[0]*(n+1)
                d[j][t]=1
    else:
        flag=1


