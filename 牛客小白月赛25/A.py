n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
cnt=0
if n<=x:
    print(sum(a))
else:
    aoe=a[x]
    cnt+=(aoe*x)
    for i in a[:x]:
        cnt+=(i-aoe)
    print(cnt)