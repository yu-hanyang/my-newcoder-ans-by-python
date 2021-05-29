n=int(input())
a=list(map(int,input().split()))
a.sort()
if(n<a[-1]):
    print(-1)
else:
    a=a[:n-a[-1]]
    cnt=ans=0
    for i in a:
        cnt+=1
        if(cnt>=i):
            ans+=1
            cnt=0
    print(ans+1)