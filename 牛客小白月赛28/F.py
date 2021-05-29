n,m=map(int,input().split())
p1=[]
p2=[]
for _ in range(n):
    a,b=map(int,input().split())
    p1.append((a,b,a+b))
    p2.append((a,b,m*a+b))
p1.sort(key=lambda x:x[2])
p2.sort(key=lambda x:x[2])
out=max((p1[0][2]+p1[1][2]),(p2[0][2]+p2[1][2]))
print(out if out>0 else 0)