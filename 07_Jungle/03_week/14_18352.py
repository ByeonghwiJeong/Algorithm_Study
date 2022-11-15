'''
< 특정 거리의 도시 찾기 > 
https://www.acmicpc.net/problem/18352
문제) 
- 어떤 나라에는 1 ~ N번까지의 도시
- M개의 단방향 도로
- X도시에서 출발해서 최단거리가 K인 모든 도시들의 번호 출력
입력)
- 1     : N, M, K, X \
    - N : 도시의 개수 [2 \ 300,000]
    - M : 도로의 개수 [1 \ 1,000,000]
    - K : 거리 정보 [1 \ 300,000]
    - X : 출발 도시의 번호 [1 \ N]
- 2[M]  : A, B ~ A에서 B
출력)
- 최단거리 도시 출력 or 없으면 -1
'''
from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
visited = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
ans = []
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)

def bfs(x):
    visited[x] = 1
    q = deque()
    q.append((x, 0))
    while q:
        x, d = q.popleft()
        if d == k: ans.append(x)
        if d > k: return
        for nxt in adj[x]:
            if visited[nxt]: continue
            visited[nxt] = 1
            q.append((nxt, d + 1))
bfs(x)
if ans: print(*sorted(ans), sep='\n')
else: print(-1)