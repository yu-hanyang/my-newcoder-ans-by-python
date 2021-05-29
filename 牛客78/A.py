n={}
for _ in range(int(input())):
    a=input()
    if a in n:
        n[a]+=1
    else:
        n[a]=1
    if len(a)==2 and a[0]!=a[1]:
        aa=a[1]+a[0]
        if aa in n:
            n[aa] += 1
        else:
            n[aa] = 1


for _ in range(int(input())):
    s=input()
    print(n[s])