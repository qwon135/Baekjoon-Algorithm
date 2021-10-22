n=int(input())
num=list(map(int,input().split()))
lst=list(map(int,input().split()))

ope=[]
for i in range(4):
    for _ in range(lst[i]):
        ope.append(i)

visited=[False]*(n-1)

anwser=[]

def dfs(result,count):
    if count==len(ope):
        anwser.append(result)
        return
    for i in range(len(ope)):
        if not visited[i]:
            visited[i]=True
            if ope[i]==0:
                dfs(result+num[count+1],count+1)
                visited[i]=False
            elif ope[i]==1:
                dfs(result-num[count+1],count+1)                
                visited[i]=False                
            elif ope[i]==2:
                dfs(result*num[count+1],count+1)                      
                visited[i]=False                
            else:
                if result<0:
                    dfs(-(-result//num[count+1]),count+1)                      
                    visited[i]=False
                else:
                    dfs(result//num[count+1],count+1)                      
                    visited[i]=False
dfs(num[0],0)
print(max(anwser))
print(min(anwser))