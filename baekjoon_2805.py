import sys
input=sys.stdin.readline

n,m=map(int,input().split()) # m=필요한 나무길이 n=나무의 갯수

array=list(map(int,input().split()))

start=0
end=max(array)

result=0
while (start<=end):
    total=0
    mid=(start+end)//2 # h값을 mid로 설정하여 시작
    for i in array:
        if i>mid: # 해당 나무가 mid보다 클때만 자를 수 있다.
            total+=i-mid
    if total<m: # 자른 나무들이 m보다 작으면 작게 잘라야하므로 좌측탐색
        end=mid-1
    else: #자른 나무들이 이미 충분하면 최적의 해를 찾아야 하므로 우측탐색
        start=mid+1
        result=mid # 우선 result를 mid로 설정

print(result)