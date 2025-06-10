import sys
input=sys.stdin.readline

N= int(input())
arr=[0]*(N+1)
if N==1:
    print(1)
    sys.exit() #끝내줘야 함수를 돌지 않아 메모리 낭비 없음
if N==2:
    print(2)
    sys.exit()

def tile(N):
    arr[1]=1
    arr[2]=2

    for i in range(3,N+1):
        arr[i]=(arr[i-1]+arr[i-2])%15746 # 메모리 사용을 줄이기 위해 나머지 값을 저장한다
    return arr[N]

print(tile(N))


# 간단한 버전
# n = int(input())
# if n == 1:
#     print(1)
# else:
#     a, b = 1, 2
#     for _ in range(3, n + 1):
#         a, b = b, (a + b) % 15746
#     print(b)
