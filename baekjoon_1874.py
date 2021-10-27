from collections import deque
import sys
input=sys.stdin.readline

n=int(input())

lst=deque()
stack=[]
result=[]
for _ in range(n):
    x=int(input())
    lst.append(x)

for i in range(1,n+1):
    stack.append(i)
    result.append('+')
    while stack:
        if stack[-1]==lst[0]:
            stack.pop()
            lst.popleft()
            result.append('-')
        else:
            break
if lst:
    print('NO')
else:
    for i in result:
        print(i)

