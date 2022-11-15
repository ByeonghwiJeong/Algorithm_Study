'''
< 최소비용 구하기 > 
https://www.acmicpc.net/problem/1916
문제) 다익스트라
- N개의 도시, M개의 버스(도시이동
- A번째도시 ▶️ B번째도시 : 버스 비용최소화
- 최소 비용을 출력
입력)
- 1     : 도시의 개수N ~ [1 \ 1000]
- 2     : 버스의 개수M ~ [1 \ 100,000]
- 3[M]  : 출발도시번호, 도착도시번호, 비용

출력)
- 
'''
import heapq, sys
input = sys.stdin.readline
INF = 987654321

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

def dijkstra(s):
    q = [(0, s)]
    dist[s] = 0
    while q:
        d, x = heapq.heappop(q)
        if dist[x] < d: continue # 이미 비용이 더작은경우 pass
        for i in graph[x]: # 갈 수 있는경로 탐색
            cost = d + i[1] # 각 경로마다 비용
            if cost < dist[i[0]]: # 비용이 더 작은 경우 갱신
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(dist[end])