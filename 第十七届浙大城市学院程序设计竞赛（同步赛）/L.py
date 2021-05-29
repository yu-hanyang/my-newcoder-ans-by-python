for _ in range(int(input())):
    n,a,b=map(int,input().split())
    if n%2==0:
        print('ALL')
    elif a%2==1:
        print('UP')
    else:
        print('DOWM')