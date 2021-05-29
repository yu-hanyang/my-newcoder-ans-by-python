md=1000000007
for _ in range(int(input())):
    n,x1,y1,x2,y2=map(int,input().split())
    cnt1=((((x1*y1)+(x1*y2))*(y2-y1+1))//2)%md
    cnt2=((((x2*y1)+(x2*y2))*(y2-y1+1))//2)%md
    cnt=(((cnt1+cnt2)*(x2-x1+1))//2)%md
    print(cnt)
