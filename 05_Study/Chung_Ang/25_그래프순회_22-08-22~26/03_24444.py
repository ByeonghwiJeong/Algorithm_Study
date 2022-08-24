'''

N개의 정점과 M개의 간선으로 구성된 무방향 그래프
정점 번호는 1 ~ N번 가중치는 1
정점 R에서 시작
노드 방문 순서 출력
인접 정점은 오름차순 방문

입력)
- 1 :정점수N~[5/100,000], 간선의수M~[1/200,000], 시작정점R[1/N]
- M개 : u, v 양방향 간선 ~ [1/N]

출력)
- N개의 줄에 정수 출력 ~ i번째 줄에는 정점 i의 방문순서
'''
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
ans = [0] * (N+1)
order = 1
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort()

def bfs(start):
    global order
    q = deque()
    q.append(start)
    visited[start] = True
 
    while q:
        v = q.popleft()
        ans[v] = order
        order += 1  
        for next in graph[v]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

bfs(R)
print(*ans[1:], sep='\n')
