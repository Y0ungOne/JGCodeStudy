# from 희구님 코드

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    area = 1

    while q:
        cur = q.popleft()
        cur_x = cur[0]
        cur_y = cur[1]

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny))
                area += 1

    return area
n = int(input())
arr = [list(map(int, input())) for _ in range(n)] 
visited = [[0] * n for _ in range(n)]

group_count = 0
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            group_count += 1
            area = bfs(i, j)
            result.append(area)

result.sort()
print(group_count)

for i in result:
    print(i)
