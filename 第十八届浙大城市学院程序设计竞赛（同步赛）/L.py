n=int(input())
a=list(map(int,input().split()))
if sum(a)-max(a)>max(a):
    print('Yes')
else:
    print('No')