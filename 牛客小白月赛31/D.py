for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print((c - a + 1)*(d - b + 1))