a=input()

b=''
c=''

for i in range(len(a)):
    if '-' not in a:
        b+=a
        break
    if a[i]=='-':
        b+=a[:i]
        c+=a[i+1:]
        break
b=b.replace('+',' ').split()
c=c.replace('-',' ')
c=c.replace('+',' ').split()
b=list(map(int,b))
c=list(map(int,c))

print(sum(b)-sum(c))

