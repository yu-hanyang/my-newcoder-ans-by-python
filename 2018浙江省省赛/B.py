from collections import Counter
for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    s=list(map(int,input().split()))
    c=[]
    for i in range(n):
        c.append(d[i]-s[i])
    an=Counter(c).most_common()
    print(an[0][1])
