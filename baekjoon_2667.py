import sys
from collections import deque
input=sys.stdin.readline

t=int(input())

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(a,b):
    q=deque([])
    q.append((a,b))
    visitied[a][b]=True
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if not(0<=nx<m and 0<=ny<n):
                continue
            if not visitied[nx][ny]:
                visitied[nx][ny]=True
                if graph[nx][ny]:
                    q.append((nx,ny))
        
for _ in range(t):
    m,n,k=map(int,input().split())
    graph=[[0]*n for _ in range(m)]
    visitied=[[False]*n for _ in range(m)]
    for _ in range(k):
        a,b=map(int,input().split())
        graph[a][b]=1
    count=0
    for i in range(m):
        for j in range(n):
            if not visitied[i][j] and graph[i][j]:
                count+=1
                bfs(i,j)
    print(count)