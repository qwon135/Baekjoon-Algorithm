import sys
input=sys.stdin.readline

n=int(input())
lst=list(input().rstrip() for _ in range(n))

lst=list(set(lst))
lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)