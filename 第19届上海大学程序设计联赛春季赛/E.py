for _ in range(int(input())):
    n=int(input())
    a=set(map(int,input().split()))
    out=sorted(a)
    print(sum(out[len(out)-3:len(out)]))