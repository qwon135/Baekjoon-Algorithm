import sys
from collections import deque
input=sys.stdin.readline

v=int(input())
e=int(input())

visited=[0]*(v+1)
graph=[[] for _ in range(v+1)]

for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q=deque([start])
    visited[start]=1
    while q:
        now=q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i]=1
                q.append(i)
    return print(sum(visited)-1)

bfs(1)
