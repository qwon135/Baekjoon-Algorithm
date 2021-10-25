import sys
input=sys.stdin.readline

n,k=map(int,input().split())
coins=[]

for _ in range(n):
    x=int(input())
    coins.append(x)
coins.sort(reverse=True)

result=0
for coin in coins:
    if k==0:
        break
    elif k//coin>=1:
        result+=k//coin
        k%=coin

print(result)