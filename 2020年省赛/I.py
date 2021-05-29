for _ in range(int(input())):
    ls=[]
    t=0
    maxt=0
    for i in range(int(input())):
        x,y=map(int,input().split())
        if x in ls:
            t+=1
        else:
            ls.append(x)
        if y in ls:
            t+=1
        else:
            ls.append(y)
        if t==len(ls):
            maxt=max(maxt,t)
            ls.clear()
    print(maxt)