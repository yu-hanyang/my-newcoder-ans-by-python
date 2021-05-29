# for _ in range(int(input())):
#     n,q=map(int,input().split())
#     a=[]
#     b=[]
#     sum_a=[0]
#     sum_b=[0]
#     for i in range(n):
#         a1,b1=map(int,input().split())
#         a.append(a1)
#         sum_a.append(sum_a[i]+a1)
#         b.append(b1)
#         sum_b.append(sum_b[i]+b1)
#     f=list(map(int,input().split()))
#     for i in range(q):
#         x=int(input())
#         if x==1:
#             print(a[0],b[0])
#         else:
#             t=f[x-2]
#             print(sum_a[t]+a[x-1],sum_b[t]+b[x-1])
for _ in range(int(input())):
    n, q = map(int, input().split())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    needs = list(map(lambda x: x-1, map(int, input().split())))
    for idx, need in enumerate(needs):
        lst[idx+1][0] += lst[need][0]
        lst[idx+1][1] += lst[need][1]
    check = []
    for _ in range(q):
        print(*lst[int(input())-1])
