import sys
from collections import deque
input=sys.stdin.readline

m,n,h=map(int,input().split())
graph=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]

def bfs(lst):
    q=deque()
    for i in lst:
        q.append(i)
    while q:
        x,y,z=q.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if not(0<=nx<h and 0<=ny<n and 0<=nz<m):
                continue
            if graph[nx][ny][nz]==-1:
                continue
            if graph[nx][ny][nz]==0:
                q.append((nx,ny,nz))
                graph[nx][ny][nz]=graph[x][y][z]+1

lst=[]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1:
                lst.append((i,j,k))
bfs(lst)

def result():
    anwser=0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k]==0:
                    return print(-1)
                anwser=max(anwser,graph[i][j][k])
    return print(anwser-1)

result()