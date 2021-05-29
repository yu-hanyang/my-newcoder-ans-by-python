for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    t=0
    max_t=0
    for i in range(n):
        while a[i]-a[t]>k:
            t+=1
        max_t=max(max_t,i-t+1)
    print(max_t)
