from collections import Counter
def allFactor(n):
    if n == 0: return [0]
    if n <=3: return [1]
    tmp = n
    rlist = [1]
    i = 2
    while i <= tmp:
        if tmp % i == 0:
            if i != rlist[-1]:
                rlist.append(i)
            tmp = tmp // i
            i = 2
            continue
        i += 1
    return rlist if n != rlist[-1] else rlist[:-1]

n,q=map(int,input().split())
a=list(map(int,input().split()))
d={}
for i in a:
    for j in allFactor(i):
        if j in d:
            d[i]+=1
        else:d[i]=1
for i in range(q):
    l,r,x=map(int,input().split())
    t=0
    print(t)