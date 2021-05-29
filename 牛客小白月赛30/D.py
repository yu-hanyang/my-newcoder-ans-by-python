n=int(input())
if n<4:
    print(-1)
else:

    prime = [2]
    for i in range(2, n + 1):
        for x in prime:
            if i % x == 0:
                break
        else:
            prime.append(i)
    print(len(prime)+2)