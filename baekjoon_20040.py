import sys
input=sys.stdin.readline

n,m = map(int,input().split())

parent = list(range(n))

def find(x):
    if parent[x] != x:
        parent[x] =find(parent[x])
    return parent[x]

def union(a,b):
    if a < b:
        parent[b] = a
    else: 
        parent[a] = b

result = 0
for i in range(m):
    a, b=map(int,input().split())
    a = find(a)
    b = find(b)
    if a == b:
        result = i+1
        break
    else:
        union(a, b)

print(result)
    
