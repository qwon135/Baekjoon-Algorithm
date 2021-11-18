import sys
input = sys.stdin.readline
t = int(input())

def find(x):
    if x not in parent:
        parent[x] = x
        friends[x] = 1
        return x
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    if a == b:
        print(friends[a])
        return
    lst=[a,b]
    lst.sort()
    parent[lst[0]] = lst[1]
    friends[lst[1]] += friends[lst[0]]
    print(friends[lst[1]])
for _ in range(t):
    parent = {}
    friends = {}    
    n = int(input())
    for _ in range(n):
        a, b= input().split()
        union(find(a), find(b))