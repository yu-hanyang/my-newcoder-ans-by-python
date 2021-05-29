for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    out=0
    d={}
    for i in a:
        b=i*2
        if b in d:
            out+=d[b]
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(out)