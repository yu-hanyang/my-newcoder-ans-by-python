n,m=map(int,input().split())
d={}
flag=1
for i in range(n):
    s,a=input().split()
    d[s]=int(a)
for i in range(m):
    food_book=list(input().split())
    k=int(food_book[0])
    if flag==0:
        break
    for j in range(k):
        food=food_book[j*2+1]
        num=int(food_book[(j+1)*2])
        d[food]-=num
        if d[food]<0:
            flag=0
            break
if flag==1:
    print('YES')
    for i in d:
        if d[i]>0:
            print(i,d[i])
else:print('NO')
