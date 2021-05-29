for _ in range(int(input())):
    n,k=map(int,input().split())
    pos=list(map(int,input().split()))
    pos.sort()
    if len(pos)==1:
        print(k)
    else:

        t=0
        for i in range(1,len(pos)):
            xs=pos[i]-pos[i-1]
            t=t+xs*xs
        print(t+k)