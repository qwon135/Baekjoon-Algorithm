import sys
input=sys.stdin.readline


k,n=map(int,input().split()) # 만들어야하는 랜선의 갯수 N, 이미있는 랜선 갯수 K


array=[]
for _ in range(k):
    x=int(input())
    array.append(x)

start=1
end=max(array)
result=0 # 원하는 최적의 전선 길이


while (start<=end):
    total=0
    mid=(start+end)//2
    for i in array:
        total+=i//mid
    # 만약 total이 n개 보다 작은 경우(더 작게 잘라야함)
    if total<n:
        end=mid-1
    # total이 k보다 같거나 큰 경우
    # (더 크게 잘라야며 이미 n개 이더라도 최적값을 찾기위해 더크게 잘라봄)
    else:
        result=mid # 우선 값 저장
        start=mid+1
print(result)