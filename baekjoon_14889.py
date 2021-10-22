n=int(input())

graph=[list(map(int,input().split())) for _ in range(n)]
visited=[False]*n

stack=[]
def score_div(stack):
    linkteam=0
    startteam=0
    not_stack=[]
    for i in range(n):
        if i not in stack:
            not_stack.append(i)

    for i in stack:
        for j in stack:
            linkteam+=graph[i][j]
    
    for i in not_stack:
            for j in not_stack:
                startteam+=graph[i][j]
    return max(linkteam,startteam)-min(linkteam,startteam)

        
result=1e9

def dfs(start,count):
    global result
    if count==n//2:
        result=min(result,(score_div(stack)))
        return
    for i in range(start,n):
        if not visited[i]:
            visited[i]=True
            stack.append(i)
            dfs(i,count+1)
            visited[i]=False
            stack.pop()
dfs(0,0)

print(result)