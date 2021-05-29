n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

aa=sorted(a,reverse=True)
bb=sorted(b,reverse=True)
t=0
for i in bb:
    if aa[0]>i:
        aa.pop(0)
        t+=1
print(t)#aa赢