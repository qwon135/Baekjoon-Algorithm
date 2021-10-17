import sys
input=sys.stdin.readline
n,k=map(int,input().split())

graph=[]

for i in range(n):
    a,b=map(int,input().split())
    graph.append([a,b])

dp=[[0 for _ in range(k+1)] for _ in range(n+1)]

graph.sort()
weight=[0]
value=[0]

for i in graph:
    weight.append(i[0])
    value.append(i[1])



for i in range(n+1):
    for j in range(k+1):
        if weight[i]>j:
            dp[i][j]=dp[i-1][j]
        else:            
            dp[i][j]=max(dp[i-1][j-weight[i]]+value[i],dp[i-1][j])

print(dp[n][k])
# for i in range(n):
#     for j in range(k+1):
#         print(dp[i][j],end=' ')
#     print()

# dp[i][j]의 정의 : 처음~ i번까지 물건을 살피고 배낭 용량이 j 일때의 배낭 value의최댓값
# 그렇다면 정답은 dp[n][k] 이다.n=가방 갯수, k=배낭 용량이므로
# i번째 물건은 weight[i]의무게와 value[i] 의 무게,가치를 갖는다.
# j용량 가방에 i번째 물건을 넣으면 답은 dp[i-1][j-weight[i]]+value[i]이다.
# -> 여기서 (i-1)번째 물건을 (j-weight[i])용량 가방에 담는 밸류와
# -> weight[i]인 i번째물건을 넣는 경우의 가치가 큰것을 가져온다.
# j용량 가방에 i번째 물건을 넣지 못한다면 답은 dp[i-1][j]

# 예시)

# 용량 6인 배낭에 i=3번째 물건을 넣지 않을때 최대값은 d[2][6]이다.
# 즉 용량 6인 배낭에 i=3번째 물건을 넣을때 값은 dp[2][6-w[3]]+v[3]=dp[2][3]+v[3]이다.
# 쉽게말해 i번째 물건을 넣을때와 넣치 않았을 때, 둘중 더 가치가 큰것을 가져오면된다.