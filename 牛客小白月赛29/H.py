for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    r_r=pow(((x2-x1)**2+(y2-y1)**2),0.5)
    if r_r<=r1+r2 and r_r>=abs(r1-r2):
        print('Yes')
    else:
        print('No')