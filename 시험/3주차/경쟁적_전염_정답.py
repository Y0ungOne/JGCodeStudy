# 매 초마다 번호가 낮은 종류의 바리어스부터 먼저 증식한다.
# 동시에 일어난다.
# from 희구님 코드


from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus.append((arr[i][j], 0, i, j))  # (번호, 시간, x, y)

virus.sort()  
q = deque(virus)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    num, time, x1, y1 = q.popleft()
    if time == s:
        break
    for i in range(4):
        nx = x1 + dx[i]
        ny = y1 + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            arr[nx][ny] = num
            q.append((num, time + 1, nx, ny))

print(arr[x-1][y-1])