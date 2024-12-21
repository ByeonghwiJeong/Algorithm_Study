"""
https://www.acmicpc.net/problem/1260
제목: DFS와 BFS

문제)
- 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성
- 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문 ->>> 정렬
- 더 이상 방문할 수 있는 점이 없는 경우 종료
- 정점 번호는 1번부터 N번까지

입력)
- N, M, V (정점의 개수, 간선의 개수, 시작 정점 번호)
    - N ~ [1 \ 1000]
    - M ~ [1 \ 10_000]
- M줄의 간선 정보 (양방향)

입력예시)
4 5 1
1 2
1 3
1 4
2 4
3 4
출력예시)
1 2 4 3
1 2 3 4
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)] # 1부터 시작

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in range(1, N+1):
    graph[i].sort()


def dfs(start):
    # global visited, result
    visited[start] = 1
    result.append(str(start))
    for i in graph[start]:
        if visited[i]: continue
        dfs(i)
    return

def bfs(start):
    # global visited, result
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        result.append(str(now))
        for i in graph[now]:
            if visited[i]: continue
            q.append(i)
            visited[i] = 1

    return 

visited = [0] * (N + 1)
result = []
dfs(V)
print(" ".join(result))
visited = [0] * (N + 1)
result = []
bfs(V)
print(" ".join(result))