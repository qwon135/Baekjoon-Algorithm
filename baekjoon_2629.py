import sys
input = sys.stdin.readline

n = int(input()) # 추의 개수
weights = [0] + list(map(int,input().split())) # 추의 무게들
k = int(input()) # 구슬의 개수
beads = list(map(int,input().split())) # 구슬의 무게들

dp = [0]*(sum(weights)+1)

for i in range(1,n+1): # i번째 추까지만 사용하는 경우
    for j in range(1,len(dp)):
        if dp[j]:
            dp[j-weights[i]] = 1
            if j+weights[i] < len(dp):
                dp[j+weights[i]] = 1
    dp[weights[i]] = 1
print(dp)
    
        