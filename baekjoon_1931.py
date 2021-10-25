import sys
input=sys.stdin.readline

n=int(input())

lst=[]
for _ in range(n):
    a,b=map(int,input().split())
    lst.append((a,b))

lst.sort()

end=lst[0][1]
result=1
for i in range(1,len(lst)):
    if lst[i][0]>=end:
        end=lst[i][1]
        result+=1
    elif lst[i][1]<end:
        end=lst[i][1]        
print(result)