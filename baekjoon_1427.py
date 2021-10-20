import sys
input=sys.stdin.readline

n=list(input().rstrip())
n=list(map(int,n))

n.sort(reverse=True)

for i in n:
    print(i,end='')