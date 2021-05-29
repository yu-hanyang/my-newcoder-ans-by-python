for _ in range(int(input())):
    n=int(input())
    r=0
    l=[]
    l_r=[0]
    for i in range(7):
        L,R=map(int,input().split())
        l.append([L,R])
        r+=R
    if r<n:
        print(0)
    else:
        sl=0
        l.sort(key=lambda x:x[0])
        for i in l:
            l_r.append(i[1]-i[0])

        for i in range(len(l)):
            n-=l[i][0]
            if n<0 :
                if n+l[i][0]<=l_r[i+1]:
                    print(i)
                    break
                else:
                    print(0)
                    break
            elif i==6 :


                print(7)



