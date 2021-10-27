from collections import deque
import sys
input=sys.stdin.readline


def bfs():
    q=deque()
    q.append(n)
    while q:
        now=q.popleft()
        if now==k:
            return
        for i in (now-1,now+1,now*2):
            if 0<=i<100001 and dp[i]==0:
                dp[i]=dp[now]+1
                q.append(i)

n,k=map(int,input().split())
dp=[0]*100001

bfs()
print(dp[k])