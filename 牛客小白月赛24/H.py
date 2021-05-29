for _ in range(int(input())):
    n=int(input())
    d={}
    t=0
    s_0=[]
    flag=0
    for i in range(n):
        a,b,c=map(int,input().split())
        if c==1:
            if (a not in d) and (b not in d):
                t+=1
                d[a]=t
                d[b]=t
            elif (a in d) and (b not in d):
                d[b]=d[a]
            elif (b in d) and (a not in d):
                d[a]=d[b]
            else:
                if d[a]!=d[b]:
                    flag=1
        else:
            s_0.append([a,b])

    if len(s_0)==0:
        print('YES')
    elif flag==1:
        print('NO')
    else:

        for i in s_0:
            if (i[0] not in d) or (i[1] not in d):
                continue
            if d[i[0]]==d[i[1]]:
                flag=1
                break
        if flag==0:
            print('YES')
        else:print('NO')