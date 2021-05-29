n,m=map(int,input().split())
if n!=m:
    s=list(map(int,input().split()))
    sum_s=sum(s)
else:
    sum_s=0
max_s=(sum_s+5*m)/n
min_s=(sum_s+m)/n
print('%.5f %.5f'%(min_s,max_s))