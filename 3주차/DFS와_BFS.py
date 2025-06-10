from collections import deque
import sys
input= sys.stdin.readline

# import sys
# sys.stdin = open("input.txt","r")
N,M,V= list(map(int,input().split()))
graph = [[] for _ in range(N + 1)]   # 인접 리스트 (1-indexed)

# 간선 입력 받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것부터 방문하도록 정렬
for i in range(1, N + 1):
    graph[i].sort()

def dfs(start, graph):
    visited = [False] * (len(graph) + 1)  # 노드 방문 여부 기록용 (0-index는 사용 안 할 수도 있음)
    stack = [start]                       # 탐색 시작 노드를 스택에 넣음

    while stack:                          # 스택이 빌 때까지 반복 (탐색할 노드가 남아 있음)
        node = stack.pop()                # 스택의 top 노드를 꺼냄

        if not visited[node]:             # 아직 방문하지 않았다면
            visited[node] = True          # 방문 표시
            print(node, end=' ')          # 현재 노드 출력

            # 연결된 이웃 노드들을 역순으로 push
            # 스택은 LIFO(후입선출) 구조이므로,
            # 역순으로 넣어야 번호가 작은 노드부터 탐색됨
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]: # 아직 방문하지 않은 이웃 노드만 추가
                    stack.append(neighbor)



def bfs(start, graph):
    visited = set()               # 이미 방문한 노드를 기록할 집합
    queue = deque([start])        # BFS에 사용할 큐. 시작 노드를 먼저 넣어줌
    visited.add(start)            # 시작 노드는 방문했다고 표시

    while queue:                  # 큐에 탐색할 노드가 남아 있는 동안 반복
        node = queue.popleft()    # 큐의 맨 앞에서 노드를 꺼냄 (가장 먼저 들어온 것)
        print(node, end=' ')       # 꺼낸 노드를 방문했으니 출력

        # 현재 노드와 연결된 이웃(자식) 노드들을 하나씩 확인
        for neighbor in graph[node]:
            if neighbor not in visited:    # 아직 방문하지 않은 이웃 노드라면
                visited.add(neighbor)      # 방문했다고 표시하고
                queue.append(neighbor)     # 큐에 넣어 다음에 탐색하도록 준비

dfs(V, graph)
print()
bfs(V,graph)