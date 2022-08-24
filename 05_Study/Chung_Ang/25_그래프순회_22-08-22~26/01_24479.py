'''
< 무방향 그래프 >
정점번호 1 ~ N 가중치 1
정점R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 방문순서
인점 정점은 오름차순으로 방문

입력)
    - N [5 ~ 100,000] M [1 ~ 200,000] R [1 ~ N]
    - M개 줄에 간선 정보 u v가  
'''
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
ans = [0] * (N + 1)
order = 1 # 순서
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort()

def dfs(graph, v, visited):
    global order
    visited[v] = True
    ans[v] = order # check
    order += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, R, visited)

print(*ans[1:])