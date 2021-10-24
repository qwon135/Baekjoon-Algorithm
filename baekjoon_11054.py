n=int(input())
dp=[0]*n
dp_reverse=[0]*n
graph=list(map(int,input().split()))
graph_revrse=graph[::-1]

for i in range(n):
    for j in range(n):
        if graph[i]>graph[j] and dp[i]<dp[j]:
            dp[i]=dp[j]       
    dp[i]+=1

for i in range(n):
    for j in range(n):
        if graph_revrse[i]>graph_revrse[j] and dp_reverse[i]<dp_reverse[j]:
            dp_reverse[i]=dp_reverse[j]       
    dp_reverse[i]+=1

dp_reverse=dp_reverse[::-1]

result=0
for i in range(n):
    result=max(result,dp[i]+dp_reverse[i])

print(result-1)