'''
< 이분 그래프 > 
https://www.acmicpc.net/problem/1707
문제) 
< Bipartite Graph >
- 그래프 정점의 집합을 둘로 분할
- 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할
- 이분그래프를 판별해라!!!
입력)
- 1     : 테스트 케이스 K
- 2     : 정점수V, 간선의개수E
    - 정점 1번 ~ V번
출력)
'''
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x):
    global visited, ret
    for nxt in adj[x]:
        if not visited[nxt]:
            visited[nxt] = 2 if visited[x] == 1 else 1 
            dfs(nxt)
        elif visited[nxt] == visited[x]:
            ret = 0
    return

for _ in range(int(input())):
    v, e = map(int, input().split())
    visited = [0] * (v + 1)
    adj = [[] for _ in range(v + 1)]
    ret = 1 # True
    for _ in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    for i in range(1, v + 1):
        if visited[i]: continue
        if not ret: break
        visited[i] = 1
        dfs(i)
    if ret: print('YES')
    else: print('NO')
