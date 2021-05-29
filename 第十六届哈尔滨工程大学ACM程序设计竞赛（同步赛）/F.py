n,m=map(int,input().split())

for i in range(n):
    l,r=map(float,input().split())
    if r>max_r:
        max_r=r
print(max_r)