n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
d=list(map(int,input().split()))
v=list(map(int,input().split()))
d_v={}
for i in range(m):
    if d[i] in d_v:
        d_v[d[i]]=max(d_v[d[i]],v[i])
    else:d_v[d[i]]=v[i]
d_=sorted(d_v.keys())
out=0
for i in a:
    vv=0
    for j in d_:
        if j>=i:
            break
        vv=max(vv,d_v[j])
    out+=vv
print(out)
