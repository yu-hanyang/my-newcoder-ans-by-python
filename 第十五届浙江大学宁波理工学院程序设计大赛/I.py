for _ in range(int(input())):
    n=int(input())
    t=[]
    z=[]
    p=[]
    for i in range(n):
        a=list(input().split())
        if a[2]=='Terran':
            t.append(int(a[0]))
        elif a[2]=='Zerg':
            z.append(int(a[0]))
        else:
            p.append(int(a[0]))
    r=list(input().split(','))
    if r[0]=='Zerg' and r[1]=='Terran':
        # print(*z,end=' ')
        # print(*t,end=' ')
        # print(*p)
        print(*(z+t+p))

    elif r[0]=='Terran' and r[1]=='Zerg':
        print(*(t+z+p))
        # print(*t, end=' ')
        # print(*z, end=' ')
        # print(*p)
    elif r[2]=='Terran' and r[1]=='Zerg':
        print(*(p+z+t))
        # print(*p, end=' ')
        # print(*z, end=' ')
        # print(*t)
    elif r[2]=='Terran' and r[0]=='Zerg':
        print(*(z+p+t))
        # print(*z, end=' ')
        # print(*p, end=' ')
        # print(*t)
    elif r[0] == 'Terran' and r[2] == 'Zerg':
        print(*(t+p+z))
        # print(*t, end=' ')
        # print(*p, end=' ')
        # print(*z)
    elif r[1]=='Terran' and r[2]=='Zerg':
        print(*(p+t+z))
        # print(*p, end=' ')
        # print(*t, end=' ')
        # print(*z)


