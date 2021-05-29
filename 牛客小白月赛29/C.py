n=int(input())
if n&1:
    print(-1)
else:
    t=1
    for i in range(n**2):
        print(t,t)
        t=1-t