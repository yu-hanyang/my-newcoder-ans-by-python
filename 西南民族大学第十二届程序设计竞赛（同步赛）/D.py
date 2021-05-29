n,r=map(int,input().split())
a=[]
b=[]
c=[]
for i in range(0,n):
    a1,b1,c1=map(int,input().split())
    a.append(a1)
    b.append(b1)
    c.append(c1-a1)

fs=r-sum(a)
if fs<=0:
    print(0)
else:
    t=0
    while fs>0:
        wz=b.index(min(b))
        if c[wz]>=fs:
            t+=fs*b[wz]
            fs-=c[wz]
        else:
            t+=c[wz]*b[wz]
            fs-=c[wz]
    print(t)



