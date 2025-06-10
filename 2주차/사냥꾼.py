from sys import stdin
#import sys
input=stdin.readline
#sys.stdin = open("input.txt","r")
M,N,L=list(map(int, input().split()))
H=list(map(int,input().split()))
H.sort()

#data에 사대배열, start에 min값, end에 max값을 받아서 이분탐색 하는데 
# 이 경우에는 범위를 받아오기 때문에 min과 max사이에 data[mid]가 존재하는지를 확인한다. 

def binary(data,start, end):# 범위값과 배열에 대한 인자 받아옴
    # 인덱스의 이분탐색을 위한 인덱스 값을 줌
    left = 0
    right = len(data)-1
    # 이분탐색 시작
    while  left <= right:
        mid=(left+right)//2 #H배열의 중앙값을 구하고
        # 이분탐색의 과정을 거침
        if data[mid] < start:
            left = mid + 1
        elif data[mid] > end:
            right = mid - 1
        else:
            return 1
    return 0


count=0
for _ in range(N):
    a,b=list(map(int, input().split()))
    if b>L:
        continue
    # min과 max는 동물의 x,y좌표값을 통해 동물이 죽을 수 있는 사대 위치의 범위의 최대 최소값임. 따라서 min과 max안에 있는 어느 사대든 해당 x,y좌표에 있는 동물은 죽을 수 밖에 없음 
    min=a-(L-b)
    max=a+(L-b)
    # 그래서 이분탐색 안에서 min과 max사이에 사대가 있는지 없는지 검사 하면 한 동물에 대한 죽을 수 있는지 없는지 에 관한 판단이 끝남

    count+=binary(H,min,max)
    
print(count)
    
