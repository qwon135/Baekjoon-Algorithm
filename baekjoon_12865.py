import sys
input=sys.stdin.readline

n,k=map(int,input().split())

dp=[[0]*(k+1) for _ in range(n+1)]
list=[]
for _ in range(n):
    w,v=map(int,input().split())
    list.append([w,v])

list.sort()
weight=[0]+[list[i][0] for i in range(n)]
value=[0]+[list[i][1] for i in range(n)]

for i in range(n+1):
    for j in range(k+1):
        if weight[i]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-weight[i]]+value[i],dp[i-1][j])
print(dp[-1][-1])




