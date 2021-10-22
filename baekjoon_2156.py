import sys
input=sys.stdin.readline

n=int(input())

graph=[0]*10000
dp=[0]*10000
for i in range(n):
    graph[i]=int(input())

dp[0]=graph[0]
dp[1]=graph[0]+graph[1]
dp[2]=max(graph[0]+graph[1],graph[0]+graph[2],graph[1]+graph[2])
for i in range(3,n):
    dp[i]=max(dp[i-1],dp[i-3]+graph[i-1]+graph[i],dp[i-2]+graph[i])

print(max(dp[:n]))


    