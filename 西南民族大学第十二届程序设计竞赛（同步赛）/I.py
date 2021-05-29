
n=int(input())
a=[]
b=[]

for i in range(n):
    a.append(list(map(int,input().split())))
'\n'
for i in range(n):
    b.append(list(map(int,input().split())))
for i in range(n):
    c=[]
    for j in range(n):
        sz=0
        for k in range(n):
            sz=sz+a[i][k]*b[k][i]
        c.append(sz)
    print(*c)


reversed()
