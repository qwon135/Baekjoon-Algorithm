n=int(input())
lst=[]
for _ in range(n):
    a,b=map(int,input().split())
    lst.append((a,b))

lst_lambda=sorted(lst,key=lambda x:(x[1],x[0]))

for i in lst_lambda:
    print(i[0],i[1])