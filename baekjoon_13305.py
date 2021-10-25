import sys
input=sys.stdin.readline

n=int(input())
distance=list(map(int,input().split()))
cost=list(map(int,input().split()))

# min(cost)인 마을에 도착하면 종료
result,now=0,1e9

for i in range(n-1):
    if cost[i]<now:
        now=cost[i]
    result+=distance[i]*now
print(result)

