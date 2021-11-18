import sys
input = sys.stdin.readline

n,m = map(int,input().split())
memories = [0] + list(map(int,input().split()))
costs = [0] + list(map(int, input().split()))

dp = [[0]*(sum(costs)+1) for _ in range(n+1)]

for i in range(1, n+1):
    cost = costs[i]
    memory = memories[i]
    for j in range(sum(costs)+1):
        if j-cost<0:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + memory)

for i in range(1,len(dp[-1])):
    if dp[-1][i] >= m:
        print(i)
        break