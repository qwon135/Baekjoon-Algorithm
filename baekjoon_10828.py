import sys
input=sys.stdin.readline

n=int(input())
stack=[]

for i in range(n):
    x=input().rstrip()
    if x=='top':
        if stack:
            print(stack[len(stack)-1])
        else:
            print(-1)
    elif x=='size':
        print(len(stack))
    elif x=='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif x=='empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        a,b=x.split()
        b=int(b)
        stack.append(b)