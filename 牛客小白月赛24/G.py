n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
cnt=0
for i in a:
    m-=i
    if m>=0:
        cnt+=1
    else:
        break
print(cnt)