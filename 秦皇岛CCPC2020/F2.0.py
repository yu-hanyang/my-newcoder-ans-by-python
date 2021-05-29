for _ in range(int(input())):
    n,k=map(int,input().split())

    if k==1 or k>30:
        print('Case '+'#'+str(_+1)+': '+str(n))
    else:
        cnt = 0
        for i in range(1,n+1):
            first = pow(i + 1,k)
            second = pow(i,k)
            if (first > n):
                cnt += ((n - second) // i)
                break
            elif (first < n):
                cnt += ((first - second )// i) + 1
            elif (first == n):
                cnt += ((first - second )// i) + 1
                break

        print('Case '+'#'+str(_+1)+': '+str(cnt))
