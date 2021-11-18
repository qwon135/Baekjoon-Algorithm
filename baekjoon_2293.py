n, k = map(int, input().split())
coins = []
for _ in range(n):
    x = int(input())
    if x <= k:
        coins.append(x)

dp = [0]*(k+1)
dp[0] = 1

for coin in coins:
    for j in range(k):
        if j+coin > k:
            break
        dp[j+coin] += dp[j]
print(dp[-1])