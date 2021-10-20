import sys
input=sys.stdin.readline

n=int(input())
count_sort=[0]*10001

for _ in range(n):
    x=int(input())
    count_sort[x]+=1

for i in range(1,10001):
    for _ in range(count_sort[i]):
        print(i)