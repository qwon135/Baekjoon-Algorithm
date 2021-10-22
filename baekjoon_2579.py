n=int(input())

graph=[0]*300
for i in range(n):
    graph[i]=int(input())

dp=[0]*300

dp[0]=graph[0]
dp[1]=graph[0]+graph[1]
dp[2]=graph[2]+(max(graph[0],graph[1]))

for i in range(3,n):
    dp[i]=max(dp[i-2]+graph[i],dp[i-3]+graph[i-1]+graph[i])

print(dp[n-1])

