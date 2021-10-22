from collections import deque
import sys
input=sys.stdin.readline
# 그래프의 정점의 집합을 둘로 분할하여
# 각집합에 속한 정점 끼리는 서로 인접하지 않도록 분할할 수 있을때 
# ->이분그래프 라고 한다.
# 그래프가 입력될때 이분그래프인지 아닌지 판별하라

def bfs(n):
    visited[n]=1
    queue=deque()
    queue.append(n)
    while queue:
        n=queue.popleft()
        for i in graph[n]:
            if not visited[i]:
                visited[i]=visited[n]*-1
                queue.append(i)
            elif visited[i]==visited[n]:
                return False
    return True
                

t=int(input()) # 테스트케이스
for _ in range(t):
    v,e=map(int,input().split()) #정점 v 간선 e
    graph=[[] for _ in range(v)]
    visited=[0]*v
    for _ in range(e):
        x,y=map(int,input().split())
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)
    result=True
    for start in range(v):
        if not visited[start]:
            if not bfs(start):
                result=False
                break
    if result:
        print('YES')
    else:
        print('NO')