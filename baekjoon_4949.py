import sys
input=sys.stdin.readline

while True:
    x=input().rstrip()
    if x=='.':
        break
    stack_1=0
    stack_2=0
    for i in range(len(x)):
        if x[i]=='(':
            stack_1+=1
        elif x[i]==')':
            stack_1-=1
            if stack_1<0:
                print('NO')
                break
        elif x[i]=='[':
            stack_2+=1
        elif x[i]==']':
            stack_2-=1
            if stack_2<0:
                print('NO')
                break
    if stack_1>=0 and stack_2>=0:   
        if stack_1==0 and stack_2==0:
            print('YES')
        elif stack_1>0 or stack_2>0:
            print('NO')