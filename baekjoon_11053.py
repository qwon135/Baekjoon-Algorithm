n=int(input())
dp=[0]*n
graph=list(map(int,input().split()))

for i in range(n):
    for j in range(n):
        if graph[i]>graph[j] and dp[i]<dp[j]:
            dp[i]=dp[j]       
    dp[i]+=1
print(max(dp))