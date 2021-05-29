for _ in range(int(input())):
    op,a,b=map(int,input().split())
    if op==1:
        print(a+b)
    elif op==2:
        print(a-b)
    elif op==3:
        print(a*b)
    elif op==4:
        print(a//b)