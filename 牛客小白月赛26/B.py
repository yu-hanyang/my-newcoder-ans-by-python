for _ in range(int(input())):
    a,b,c=map(int,input().split())
    bc=b*c
    if (bc)%a==0:
        print((bc)//a)

    else:print(-1)