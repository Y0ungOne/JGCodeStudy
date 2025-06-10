# 상하좌우 개념은 필요없을 거 같다.
# 세로줄일 경우 밑으로 내려가면 확인
# 가로줄일 경우 오른쪽으로 이동하면 확인 한다.
# 줄이 이어지지않을 경우 count
# 희구님 코드
from collections import deque

def bfs(x, y, line):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cur_x, cur_y = q.popleft()

        if line == '|':
            next_x = cur_x + 1
            if 0 <= next_x < n and not visited[next_x][cur_y] and arr[next_x][cur_y] == '|':
                visited[next_x][cur_y] = True
                q.append((next_x, cur_y))

        else:  
            next_y = cur_y + 1
            if 0 <= next_y < m and not visited[cur_x][next_y] and arr[cur_x][next_y] == '-':
                visited[cur_x][next_y] = True
                q.append((cur_x, next_y))


n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]  # 한 줄에 문자열로 받기

visited = [[False] * m for _ in range(n)]
total = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j, arr[i][j])
            total += 1

print(total)