s=input()
lb={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
st=0
sz=[]
for i in s:
    if i>='A' and i<='Z':
        sz.append(lb[i])

    elif i in '0123456789':
        st=st*10+int(i)
    if (i in lb ) and st!=0:
        sz.pop()

        sz.append(st*sz.pop())
        sz.append(lb[i])
        st=0
    elif i==')':
        sz.append(st*sz.pop())
        st=0
    if i==')':
        x=sum(sz)
        sz.clear()
        sz.append(x)
if st!=0:
    sz.append(st * sz.pop())
    st = 0
print(sum(sz))


