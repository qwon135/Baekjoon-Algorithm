import sys
input=sys.stdin.readline

n=int(input())

for _ in range(n):
    stack=0
    x=input().rstrip()
    for i in range(len(x)):
        if x[i]=='(':
            stack+=1
        else:
            stack-=1
            if stack<0:
                print('NO')
                break
    if stack==0:
        print('YES')        
    elif stack>0:
        print('NO')
