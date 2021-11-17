import sys
input = sys.stdin.readline

n = int(input()) # 추의 개수
weights = [0] + list(map(int,input().split())) # 추의 무게들
k = int(input()) # 구슬의 개수
beads = list(map(int,input().split())) # 구슬의 무게들

dp = [[0]*(sum(weights)+1) for _ in range(n+1)]

for i in range(1,n+1): # i번째 추까지만 사용하는 경우
    dp[i][weights[i]] = 1
    for j in range(1,sum(weights)+1): # 해당 무게         
        if dp[i-1][j]:
            dp[i][j] = 1
            dp[i][abs(weights[i]-j)] = 1
            if j+weights[i]<=sum(weights):
                dp[i][j+weights[i]] = 1            
    
for bead in beads:
    if bead>sum(weights) or (not dp[n][bead]):
        print('N',end=' ')
    else:
        print('Y',end=' ')    
    
        