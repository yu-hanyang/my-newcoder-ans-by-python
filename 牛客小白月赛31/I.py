from collections import Counter
s=input()
# if len(Counter(s).most_common())==1:
#     print('1')
# else:
for i in range(len(s)//2+1):
    if s[i]!=s[len(s)-i-1]:
        print(len(s))
        break
else:print(len(s)-1)