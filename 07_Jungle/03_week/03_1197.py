'''
< 최소 스패닝 트리 > 
https://www.acmicpc.net/problem/1197
문제 : 그래프 MST구하기
- Minimum Spanning Tree
- 양방향그래프

입력)
- 1     : 정점개수 V, 간선개수 E
- 2     : A, B, C 
    - A번정점과 B번정점이 가중치C인 간선으로 연결됨
출력)
- 최소비용출력
'''
import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split())
n = [[] for _ in range(v + 1)]
visited = [0] * (v + 1)
ans = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    n[a].append((c, b))
    n[b].append((c, a))
hq = [(0, 1)] # 1번 노드에서 시작
while hq:
    w, _node = heapq.heappop(hq)
    if visited[_node]: continue
    visited[_node] = 1
    ans += w
    for nxt in n[_node]:
        if visited[nxt[1]]: continue
        heapq.heappush(hq, nxt)
print(ans)
'''
패스
'''