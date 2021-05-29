n,m=map(int,input().split())
w=list(map(int,input().split()))
for _ in range(m):
    a,b,c=input().split()
    if a=='Change':
        w[int(b)-1]=int(c)
    else:
        max_lr=max(w[int(b)-1:int(c)+1])
        g=w[int(b)-1:int(c)+1].count(max_lr)
        print(max_lr,g)