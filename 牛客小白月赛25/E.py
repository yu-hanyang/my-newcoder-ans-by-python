s=input()
stack=[]
for i in s:
    if stack:
        if stack[-1]==i:
            stack.pop()
        else:stack.append(i)
    else:stack.append(i)
if stack:
    print(''.join(stack))
else:print(0)