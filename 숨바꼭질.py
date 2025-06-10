from collections import deque

def bfs(N, K):
    MAX = 100001  # 좌표 범위는 0 ~ 100000
    visited = [0] * MAX  # 방문 시간 저장

    queue = deque()
    queue.append(N)

    while queue:
        current = queue.popleft()

        if current == K:
            return visited[current]

        for next_pos in [current - 1, current + 1, current * 2]:
            if 0 <= next_pos < MAX and visited[next_pos] == 0:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

# 입력
N, K = map(int, input().split())
print(bfs(N, K))
