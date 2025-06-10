from collections import deque
import sys
input= sys.stdin.readline

# 여기도 1번 문제랑 다를 것 없는 같은 코드 입니다
# 그냥 무시하시고 넘어가시면 됩니다 
# 못 푼 문제입니다
# 남아있는 코드는 유사 미로탐색 코드 입니다
# 무시하셔도 됩니다
N=int(input())

town=[]
for i in range(N):
    line= input().strip()
    row= list(map(int, line))
    town.append(row)

#상하좌우 이동 방향
dx=[-1,1,0,0]
dy=[0,0,-1,1]        
        
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    

    while queue:
        x,y=queue.popleft()
        
        # 4방향 탐색
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
        
            # 범위 안에 있고, 길이 존재하는 칸이면
            if 0<= nx <N and 0<=ny <N and town[nx][ny]==1:
                # 이전거리 +1 저장 (방문 체크도 겸함)
                town[nx][ny]=town[x][y]+1
                queue.append((nx,ny))

    return town[N-1][N-1]
print(bfs(0, 0))
