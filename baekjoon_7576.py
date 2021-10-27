import sys
from collections import deque
input=sys.stdin.readline

m,n=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(lst):
    q=deque()
    for i in lst:
        q.append(i)
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if not(0<=nx<n and 0<=ny<m):
                continue
            if graph[nx][ny]==-1:
                continue
            if graph[nx][ny]==0:
                q.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1

lst=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            lst.append((i,j))
bfs(lst)

def result():
    anwser=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                return print(-1)
            anwser=max(anwser,graph[i][j])
    return print(anwser-1)

result()