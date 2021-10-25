import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

dp=[0]*n
dp[0]=lst[0]

for i in range(1,len(lst)):
    if dp[i-1]<0 and lst[i]<0:
        dp[i]=max(dp[i-1],lst[i])
    elif dp[i-1]+lst[i]<0:
        pass
    else:
        dp[i]=dp[i-1]+lst[i]
print(max(dp))


