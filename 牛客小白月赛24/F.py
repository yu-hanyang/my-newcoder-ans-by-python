d={'elephant': 1, 'tiger': 2, 'cat': 3, 'mouse': 4}
m,n=input().split()
t=0
if d[n]==1 and d[m]==2:
    t=1
elif d[n]==2 and d[m]==3:
    t=1
elif d[n]==3 and d[m]==4:
    t=1
elif d[n]==4 and d[m]==1:
    t=1

if t:
    print('tiangou txdy')
else:print('tiangou yiwusuoyou')

