from collections import deque
import sys
input= sys.stdin.readline

# import sys
# sys.stdin = open("input.txt","r")
N,M=list(map(int,input().split()))

maze=[]
for i in range(N):
    line= input().strip()
    row= list(map(int, line))
    maze.append(row)

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
        
            # 미로 범위 안에 있고, 길이 존재하는 칸이면
            if 0<= nx <N and 0<=ny <M and maze[nx][ny]==1:
                # 이전거리 +1 저장 (방문 체크도 겸함)
                maze[nx][ny]=maze[x][y]+1
                queue.append((nx,ny))
    # 도착지까지 거리 반환
    return maze[N-1][M-1]
print(bfs(0, 0))
