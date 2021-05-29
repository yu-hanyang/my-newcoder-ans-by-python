from collections import Counter
a=input()
b=input()
aa=list(Counter(a))
bb=list(Counter(b))
for i in aa:
    if i in bb:
        print('Yes')
        break
else:print('No')