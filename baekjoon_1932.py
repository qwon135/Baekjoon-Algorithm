n=int(input())

graph=[]
for _ in range(n):
    lst=list(map(int,input().split()))
    graph.append(lst)

for i in range(1,n):
    for j in range(len(graph[i])):
        if j==0:
            graph[i][j]+=graph[i-1][j]
        elif j==len(graph[i])-1:
            graph[i][j]+=graph[i-1][-1]
        else:
            graph[i][j]+=max(graph[i-1][j],graph[i-1][j-1])
print(max(graph[n-1]))
