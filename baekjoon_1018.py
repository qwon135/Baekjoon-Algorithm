n,m=map(int,input().split())
lst=[]
for _ in range(n):
    a=list(input())
    lst.append(a)

# 멀쩡한 8*8 체스판
case=[['W','B']*4,['B','W']*4]*4

result=32
count=0
for i in range(n-7):
    for j in range(m-7):
        for a in range(8):
            for b in range(8):
                if lst[i+a][j+b]!=case[a][b]:
                    count+=1
        result=min(result,count,64-count)
        count=0
print(result)