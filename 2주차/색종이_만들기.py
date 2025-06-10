import sys

sys.stdin = open("input.txt", "r")
# from sys import stdin
# input=stdin.readline
#하얀색과 파란색 네모 부분 카운트 하는 변수
white=0
blue=0
N= int(input())
paper=[]
for i in range(N):
    paper.append(list(map(int, input().split())))
    
def divide(x,y,size):
    #기준이 되는 색을 현재 구역의 왼쪽 위 칸 색으로 설정
    color=paper[x][y]
    # x행부터 x+size-1행까지 y열부터 y+size열까지 모두 순회하면서 현재 xy칸이 다른 칸과 모두 같은지 검색하는 것
    for i in range(x,x+size):
        for j in range(y,y+size):
            if paper[i][j]!=color: # 하나라도 다르면 분할
                half=size//2 # N/2 한 크기
                # 4분할 각각 재귀호출
                divide(x,y,half) #좌상
                divide(x,y+half,half) #우상
                divide(x+half,y,half) #좌하
                divide(x+half,y+half,half) #우하
                return #다르게 생긴 부분이 발견됐으면 더 이상 검사하지 않음
    # 만약 모두 같은 색이면 해당 색에 맞는 카운트 증가        
    if color==0:
        global white
        white +=1
    else:
        global blue
        blue+=1
# 전체 종이 (0,0 부터 N*N크기) 로 divide 함수 실행
divide(0,0,N)
print(blue) 





















































# paper = []
# N = int(input())
# for _ in range(8):
#     paper.append(list(map(int, input().split())))
# white = 0
# blue = 0


# #     global white,blue
# N_len = 0
# for i in range(N):
#     for j in range(N - 1):
#         if paper[i][j] != paper[i][j + 1]:
#             divide(paper)
#             break


# def divide(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     divide([row[:mid] for row in paper[:mid]])
#     divide([row[mid:] for row in paper[:mid]])
#     divide([row[:mid] for row in paper[mid:]])
#     divide([row[mid:] for row in paper[mid:]])
