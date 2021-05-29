t = int(input())
md = 998244353
def func(n):
    return pow(2,n,md)-1
for i in range(0,t):
    n = int(input())
    Sum = 1
    for j in range(0,n):
        a,b = map(int,input().split())
        S = (func(a) + func(b))%md
        Sum = S * Sum % md
    print(int(Sum))