n=int(input())
lst=[0]+list(map(int,input().split()))
m=int(input())
dp=[[0]*(n+1) for _ in range(n+1)]

for i in range(2,n+1):
    for j in range(1,n+1-(i-1)):
        if lst[j] == lst[j]:

            dp[j][j+i-1] = 