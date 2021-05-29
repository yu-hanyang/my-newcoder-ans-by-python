for _ in range(int(input())):
    n=int(input())
    t=0
    for i in range(n):
        x,y=map(int,input().split())


        if t>y:
            n=n+t-y
            t=y
        elif y<x:
            n=n+x-t
            t=x

    print(n)