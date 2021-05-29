for _ in range(int(input())):
    lst = list(map(int, input().split()))
    lst.sort()
    flag = 0
    for i in range(2, 6):
        # print(lst[i], lst[i-1], lst[0])
        if lst[i] - lst[i-1] < lst[0]:
            lst2 = []
            lst2.extend(lst[1:i-1])
            lst2.extend(lst[i+1:])
            # print('i', i, 'lst2', lst2)
            if sum(lst2[:2]) > lst2[2]:
                print('Yes')
                flag = 1
                break
    if flag == 0:
        print('No')