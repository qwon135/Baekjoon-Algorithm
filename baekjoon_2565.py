n=int(input())
list=[]
for _ in range(n):
    a,b=map(int,input().split())
    list.append((a,b))
list.sort()
list_b=[list[i][1] for i in range(len(list))]
dp=[0]*n

for i in range(n):
    for j in range(n):
        if list_b[i]>list_b[j] and dp[j]>dp[i]:
            dp[i]=dp[j]
    dp[i]+=1
print(n-max(dp))

