import sys
from collections import deque
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    lst=deque(map(int,input().split()))
    q=deque(range(n))
    count=0
    while q:
        if lst[q[0]]==max(lst):
            if q[0]==m:
                print(count+1)
                break
            lst[q[0]]=0
            q.popleft()
            count+=1
        else:
            q.append(q.popleft())
