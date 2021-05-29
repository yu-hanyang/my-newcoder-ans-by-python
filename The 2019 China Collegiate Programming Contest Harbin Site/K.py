for _ in range(int(input())):
    n,k=map(float,input().split())
    wn=list(map(float,input().split()))
    sumwn=sum(wn)
    res=[]
    for i in wn:
        res+='%.8f' %(i+i/sumwn*k),
    print(*res)