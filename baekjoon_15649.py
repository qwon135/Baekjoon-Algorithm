import sys
input=sys.stdin.readline

n,m=map(int,input().split())

result=[]
visited=[False]*(n+1)

def dfs(v,n,m):
    if v==m:
        for i in range(m):
            print(result[i],end=' ')
        print()
        return
    for i in range(1,n+1):
        if not visited[i]:
            result.append(i)
            visited[i]=True
            dfs(v+1,n,m)
            visited[i]=False
            result.pop()
dfs(0,n,m)