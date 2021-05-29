import math

cnt = 0


def func(lis, top, dowm):
    global cnt
    cnt += 1
    l = len(lis)
    if l > 1:
        mid = (top + dowm) // 2
        i = 0
        while i < l:
            if lis[i] <= mid:

                i += 1
            else:
                break

        func(lis[:i], mid, dowm)
        func(lis[i:], top, mid + 1)


n, k = map(int, input().split())
num = list(map(int, input().split()))

if k == 1:
    print(1)
else:
    func(num, n, 1)
    print(cnt)


