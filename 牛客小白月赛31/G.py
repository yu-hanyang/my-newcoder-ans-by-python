for _ in range(int(input())):
    x,y = map(int, input().split())
    for k in range(200):
        if x**k > y:
            print(k-1)
            break
    else:
        print(-1)