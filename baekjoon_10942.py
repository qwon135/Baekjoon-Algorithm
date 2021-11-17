import sys
input = sys.stdin.readline

n=int(input())
lst=[0]+list(map(int,input().split()))
m=int(input())
dp=[[0]*(n+1) for _ in range(n+1)]

# dp[a][b] 는 a~b까지가 팰린드롬인지 아닌지를 의미
for i in range(1,n+1): # 길이를 의미
    for j in range(1,n+1-(i-1)): # j~j+i-1번째 까지 시작을 의미
        if i == 1:
            dp[j][j] = 1
        elif i == 2 and lst[j] == lst[j+1]:
            dp[j][j+1] = 1
        elif lst[j] == lst[j+i-1] and dp[j+1][j+i-2]:
            dp[j][j+i-1]=1

for _ in range(m):
    s, e = map(int,input().split())
    print(dp[s][e])
