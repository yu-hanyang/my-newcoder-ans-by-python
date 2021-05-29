n,m=map(int,input().split())
t=0
a=[i for i in range(1,n+1)]
for i in range(m):
    s=input().split()
    if s[0]=='4':
        ind=a.index(1)
        if t==0:
            print(*a[ind:],end=' ')
            print(*a[:ind])
        else:
            print(*a[ind::-1], end=' ')
            print(*a[:ind:-1])

    elif s[0]=='1':
        x=int(s[1])
        y=int(s[2])
        if t==0:
            indx=a.index(x)
            indy=a.index(y)
            tt=0
            if indx>indy:
                tt+=1
            a.insert(indy+tt,a.pop(indx))
        else:
            indx = a.index(x)
            indy = a.index(y)
            tt=-1
            if indx>indy:
                tt+=1
            a.insert(indy+tt , a.pop(indx))
    elif s[0]=='2':
        x = int(s[1])
        y = int(s[2])
        if t==1:
            indx=a.index(x)
            indy=a.index(y)
            tt=0
            if indx>indy:
                tt+=1
            a.insert(indy+tt,a.pop(indx))
        else:
            indx = a.index(x)
            indy = a.index(y)
            tt=-1
            if indx>indy:
                tt+=1
            a.insert(indy+tt , a.pop(indx))
    else:t=1-t
