import sys
input=sys.stdin.readline

n = int(input())
m = int(input())

parent = list(range(n+1))

def find(x):
    while parent[x] != x:
        x = parent[x]    
    return x

def union(a, b):    
    if a == b:
        return
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, n+1):
    graph = [0]+list(map(int,input().split()))
    for j in range(1,n+1):
        if j<i:
            continue
        if graph[j]:
            union(i,j)

plan = [find(i) for i in list(set(map(int,input().split())))]
plan = list(set(plan))

if len(plan) == 1:
    print('YES')
else:
    print('NO')