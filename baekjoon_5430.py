import sys
from collections import deque
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    command=input().rstrip()
    n=int(input())
    a=input().rstrip()[1:-1].split(',')
    if n==0:
        q=[]
    else:
        q=deque(a)
    result=True
    popleft=True
    for i in command:
        if i=='R':
            pop=not pop
        elif i=='D':
            if not q:
                result=False
                break
            if popleft:
                q.popleft()
            else:
                q.pop()
    if result:
        if popleft:
            print('[',end='')
            print(*q,sep=',',end='')
            print(']')
        else:
            q=list(q)[::-1]
            print('[',end='')
            print(*q,sep=',',end='')
            print(']')            
    else:
        print('error')
    


