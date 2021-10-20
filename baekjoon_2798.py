n,m=map(int,input().split())
cards=list(map(int,input().split()))

result=0
for i in cards:
    for j in cards:
        for k in cards:
            if i!=j and j!=k and i!=k and i+j+k<=m:
                result=max(result,i+j+k)

print(result)