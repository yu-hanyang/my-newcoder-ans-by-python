d={}
for _ in range(int(input())):
    n=input().split()
    d[n[0]]=' '.join(n[1:])
for _ in range(int(input())):
    n=input().split()
    out=[]
    for i in n:
        if i in d:
            out.append(d[i])
        else:
            out.append(i)
    print(*out)
