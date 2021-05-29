for _ in range(int(input())):
    q,n,p=map(int,input().split())
    cnt=q
    cs=q
    if q==1:
        print(n%p)
    elif n==1:
        print(q%p)
    else:
        print()
