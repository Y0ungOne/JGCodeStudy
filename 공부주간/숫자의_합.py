import sys
# input= sys.stdin.readline

N=int(input())
arr=list(map(int,input()))
result=0
for i in range(N):
    result=arr[i]+result
print(result)
# 입력받을 숫자 개수 N입력 받음
# 다음줄에 숫자 배열로 입력받기 -> 공백이 없어서 무슨 기준으로 받아오나...?
# for문에 배열 돌려서 인덱스마다 합치기
# 합친거 출력하기
