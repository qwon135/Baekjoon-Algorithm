import sys
input = sys.stdin.readline

n,m=map(int,input().split())

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

for _ in range(m):
    c,a,b = map(int,input().split())
    if c == 0:
        union(a, b)
    else:
        if a==b :
            print('YES')
            continue
        if find(a) == find(b):
            print('YES')
            continue
        print('NO')