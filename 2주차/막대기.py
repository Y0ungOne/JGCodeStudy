import sys
input=sys.stdin.readline
N=int(input())
arry=[]
for i in range(N):
    arry.append(int(input()))
#pop을 하면서 N을 -하면서 기둥 갯수 뺄거임
count=N

#맨 마지막 것을 바라보며 기둥을 세기 때문에 마지막 값을 max에다 저장
max=arry[-1]

# N-2로 시작하는 이유는 맨 마지막 이전(6개면 5번째 기둥부터 확인 하기 위해서-> 마지막거는 무조건 보이기 때문에 count에 들어가 있어야 함)
#-1까지 탐색 해야 0번째 까지 탐색 가능
#-1씩 줄어드는 for문
for j in range(N-2,-1,-1):
    #N-2번부터 j값에 들어가서 미리 넣어둔 max(마지막 값)과 비교하는 것 부터 시작.
    if max>=arry[j]:
        arry.pop(j)
        count-=1
    if max<arry[j]:
        max=arry[j]

print(count)
