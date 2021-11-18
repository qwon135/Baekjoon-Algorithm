def post_title(num,name):
    return f'[백준] {num} : {name} [파이썬]'

def tag(a):
    a=a.rstrip()
    a=a[1:-1]
    a=a.replace('[',',')
    a=a.replace(']',',')
    a=a.replace(':',',')    
    print(a)

a,b=input().split()
print(post_title(a,b))
tag(post_title(a,b))