from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().split())

result=[]
q=deque(range(1,n+1))

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())

print('<',end='')
print(*result,sep=', ',end='')
print('>')