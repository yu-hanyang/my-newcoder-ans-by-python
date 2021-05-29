for _ in range(int(input())):
    n = int(input())
    bina = bin(n)[2:]
    if '0' not in bina:
        print(len(bina))
    else:
        cm=len(bina)-1
        n-=2**cm-1
        b=bin(n)[2:]
        out=cm+b.count('1')
        print(out)
