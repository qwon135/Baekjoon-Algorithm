import sys
from collections import deque
input=sys.stdin.readline
a=input().rstrip()
q=deque(a[1:-1].split(','))
print(q)
