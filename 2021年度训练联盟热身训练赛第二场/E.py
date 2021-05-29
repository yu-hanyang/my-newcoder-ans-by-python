for _ in range(int(input())):
    n,c=map(int,input().split())
    p=0
    for i in range(n):
        s=list(map(int,input().split()))
        ss=[]
        for j in range(len(s)-1,-1,-2):
            ss.append([s[j-1]/s[j],j-1])
        ss.sort(key=lambda x:x[0])
        t=0
        k=0
        while t==0 and k<len(ss):
            if s[ss[k][1]]<=c:
                c-=s[ss[k][1]]
                p+=s[ss[k][1]+1]
                t=1
                print(ss)
                print(ss[k][1])
                print(s[ss[k][1]])
                print(c)
            k+=1

    print(p)


