for _ in range(int(input())):
    n,m=map(int,input().split())
    w=[]
    for i in range(n):
        w.append(input().split())

    w.sort(key=lambda x:int(x[1]),reverse=True)
    an=[]
    ant=[]
    antt=[]

    if n!=m:
        wz=0
        t=0
        for i in range(1,n):
            if w[i][1]==w[i-1][1] and t==0:
                t=1
                wz=i-1

            elif i==n-1 and t==1:
                ant=w[wz:i+1]
                ant.sort(key=lambda x:x[0])
                antt.extend(ant)
            elif w[i][1]!=w[i-1][1] and t==1:
                t=0
                ant=w[wz:i]
                ant.sort(key=lambda x: x[0])
                antt.extend(ant)



        # print(w)
        # print(ant)


    t=0
    H=0
    for i in range(m):
        if w[i] in antt:
            an.append(antt[t][0])
            H+=(m-i)*(int(antt[t][1]))
            t+=1
        else:
            an.append(w[i][0])
            H += (m - i ) * (int(w[i][1]))

    print(H,*an)
