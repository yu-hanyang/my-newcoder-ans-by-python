n,k,q=map(int,input().split())
for _ in range(q):
    x,y=map(int,input().split())
    cs=min(min(x,n+1-x),min(y,n+1-y))
    print(cs*k)