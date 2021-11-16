n=int(input())

lst=[(0,0)]

for _ in range(n):
    a,b = map(int,input().split())
    lst.append((a,b))
dp=[[0]*(n+1) for _ in range(n+1)]



for i in range(2,n+1):
    for j in range(1,n+1-(i-1)):
        dp[j][j+i-1] = min(dp[j][j+k]+dp[j+k+1][j+i-1]+lst[j][0]*lst[j+k][1]*lst[j+i-1][1] for k in range(i-1))

print(dp[1][n])
