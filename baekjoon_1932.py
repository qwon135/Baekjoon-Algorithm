import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

lst_set=list(set(lst))
lst_set.sort()

lst_dic={lst_set[i] : i for i in range(len(lst_set))}

print(lst_dic)

for i in lst:
    print(lst_dic[i],end=' ')
