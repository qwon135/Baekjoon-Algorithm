import sys
input=sys.stdin.readline

while True:
    x=input().rstrip()
    if x=='.':
        break
    stack=[]
    result=True
    for i in x:
        if i=='[' or i=='(':
            stack.append(i)
        elif i==']':
            if not stack:
                result=False
                break
            if stack[-1]=='[':
                stack.pop()
            else:
                result==False
                break
        elif i==')':
            if not stack:
                result=False
                break
            if stack[-1]=='(':
                stack.pop()
            else:
                result==False
                break
    if result and not stack:
        print('yes')
    else:
        print('no')
            


