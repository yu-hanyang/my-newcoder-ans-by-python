max_s=['0']
for _ in range(int(input())):
    s=input().split()
    if int(s[0])>int(max_s[0]):
        max_s=s
for i in max_s:
    print(i)
