n,m=map(int,input().split())
s_n=[0]*n
s_m=[0]*m
ho=[]
for i in range(n):
    a=list(map(int,input().split()))
    ho.append(a)
    for j in range(m):
        s_n[i]+=a[j]
        s_m[j]+=a[j]

for i in range(n):
    out=[]
    for j in range(m):
        out.append(s_n[i]+s_m[j]-ho[i][j])
    print(*out)