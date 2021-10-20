n=int(input())
lst=[0]*8001
for _ in range(n):
    x=int(input())
    lst[x]+=1

# 산술평균
average=0
for i in range(-4000,4001):
    average+=i*lst[i]
average/=n
print(int(round(average,0)))

# 중앙값
mid=n//2+1
result=-4000
count=0

while True:
    count+=lst[result]
    if count>=mid:
        break
    else:
        result+=1
print(result)

# 최빈값
mode=[]
for i in range(-4000,4001):
    if lst[i]==max(lst):
        mode.append(i)
if len(mode)>1:
    print(mode[1])
else:
    print(mode[0])
     

# 범위
rng=[]
for i in range(-4000,4001):
    if lst[i]:
        rng.append(i)
print(max(rng)-min(rng))