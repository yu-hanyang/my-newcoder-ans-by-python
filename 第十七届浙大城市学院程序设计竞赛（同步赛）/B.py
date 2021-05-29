for _ in range(int(input())):
    n=int(input())
    t=list(map(int,input().split()))
    if n==1:
        print('%.2f'%(0))
    else:
        out=0
        t.sort()
        for i in range(n-1):
            out=out+t[i]*(n-i-1)
        print('%.2f'%(out/n))

