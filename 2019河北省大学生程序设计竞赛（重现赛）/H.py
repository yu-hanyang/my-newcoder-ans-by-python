def swsum(x):
    cnt=0
    while x!=0:
        cnt+=(x%10)
        x=x//10
    return cnt

for _ in range(int(input())):
    n,k=map(int,input().split())
    y=n**k
    while y>9:
        y=swsum(y)
    print(y)

print(swsum(121))