def tag(a):
    a=a.rstrip()
    a=a[1:-1]
    a=a.replace('[',',')
    a=a.replace(']',',')
    a=a.replace(':',',')
    print(a)

tag(input())