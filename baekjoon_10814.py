n=int(input())

lst=[]

for _ in range(n):
    a,b=input().split()
    a=int(a)
    lst.append((a,b))
lst.sort(key=lambda x:x[0])

for i in lst:
    print(i[0],i[1])