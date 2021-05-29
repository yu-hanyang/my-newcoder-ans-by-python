n,s=map(int,input().split())
a=list(map(int,input().split()))
max_a=max(a)
min_a=min(a)
if s<=min_a:
    print(max_a-s)
elif s>=max_a:
    print(s-min_a)
elif max_a-s>s-min_a:
    print(s-min_a+max_a-min_a)
else:print(max_a-s+max_a-min_a)