for _ in range(int(input())):
    d=[[],[],[],[],[],[]]
    # d={0:[],1:[],2:[],3:[],4:[],5:[]}
    for i in range(6):
        s=input()
        if 'h' in s:
            d[0]+=i,
        if 'a' in s:
            d[1]+=i,
        if 'r' in s:
            d[2]+=i,
        if 'b' in s:
            d[3]+=i,
        if 'i' in s:
            d[4]+=i,
        if 'n' in s:
            d[5]+=i,

