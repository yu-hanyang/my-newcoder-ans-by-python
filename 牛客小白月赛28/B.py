for _ in range(int(input())):
    x,y=map(int,input().split())
    if x==0 and y==0:
        print('awsl')
    elif x==0:
        if y%3==0:
            print('awsl')
        else:print('yyds')
    elif y==0:
        if x%3==0:
            print('awsl')
        else:print('yyds')
    else:
        if x%3==0 and y%3==0:
            print('awsl')
        elif x%3!=0 and y%3!=0:
            print('awsl')
        else:
            print('yyds')