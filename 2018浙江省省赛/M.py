for _ in range(int(input())):
    t,n=map(int,input().split())
    a=list(map(int,input().split()))
    for i in a:
        if (i+n)%7==0:
            print('Yes')
            break
    else:
        print('No')