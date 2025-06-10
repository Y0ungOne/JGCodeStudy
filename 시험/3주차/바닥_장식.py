from collections import deque
import sys
input= sys.stdin.readline
# 안내말씀 남깁니다. 저 못풀었어요 열심히 뭐라도 해보는데 안되네요 
# 해결한 문제가 없으니 그냥 아 노력은 했구나 하고 넘어가시면 됩니다.
N,M=list(map(int,input().split()))

tile=[]
for i in range(N):
    line= input().strip()
    row= list(line)
    tile.append(row)

dx=[-1,1,0,0]
dy=[0,0,-1,1]



def bfs(x,y):
    tile_count=0
    queue=deque()
    queue.append((x,y))
    
    while queue:
        tile[x][y]=queue.popleft()
        
        
        # 상하좌우 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 타일 범위 안에 있고, '-' 이걸로 좌우 범위로 같거나 '|'이걸로 상하가 같으면 횟수 증가 X->터무니 없음 못함
            if 0<= nx<N and 0<=ny<M and (tile[nx][ny]==tile[nx][ny+1] or tile[nx][ny]==tile[nx+1][ny]):
                queue.append((nx,ny))
            else:
                tile_count+=1
                queue.append((nx,ny))
        return tile_count
    
print(bfs(0,0))