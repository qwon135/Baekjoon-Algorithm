from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int,input().rstrip())) for _ in range(n)]
visitied=[[[0]*2 for _ in range(m)]for _ in range(n)]

dx=[0,0,-1,1]
dy=[1,-1,0,0]


def bfs(x,y,crash,visited,graph):
    queue=deque()
    queue.append((x,y,crash))
    visited[x][y][crash]=1
    while queue:
        x,y,crash=queue.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][crash]
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y

            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            # 벽안부숨
            if graph[nx][ny]==0 and visited[nx][ny][crash]==0:
                queue.append((nx,ny,crash))
                visited[nx][ny][crash]=visited[x][y][crash]+1
            # 벽 부숨
            if graph[nx][ny]==1 and crash==0:
                queue.append((nx,ny,crash+1))
                visited[nx][ny][crash+1]=visited[x][y][crash]+1            
    return -1
print(bfs(0,0,0,visitied,graph))