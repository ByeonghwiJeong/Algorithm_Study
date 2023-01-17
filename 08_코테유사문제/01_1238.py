'''
< 파티 >
https://www.acmicpc.net/problem/1238
문제)
- N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.
- 어느 날 이 N명이 X~[1 \ N] 마을에 모여서 파티를 열었다.
- 총 M개의 단방향 도로들이 있고 i번째 길을 지나는 데
    - Ti ~ [1 \ 100] 시간 소비
- 각 학생은 파티에 참석하고 다시 되돌아 와야한다.
    - 최단 시간에 오고 가기를 원한다.
- 이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다.
- N명의 학생들중 오고 가는데 가장 많은 시간을 소비하는 학생은 ?
입력)
- 1     : N ~ [1 \ 1000],  M ~ [1 \ 10,000],  X
- 2[M]  : i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다. 시작점과 끝점이 같은도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.
모든 학생들은 집에서 X에 갈수 있고, 
'''
import sys, heapq
input = sys.stdin.readline
INF = 10**9

n, m, x = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    st, en, cost = map(int, input().split())
    graph[st].append((en, cost))

def dijkstra(start_node):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0

    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost: continue
        for i in graph[now]:
            next_cost = i[1] + cost
            if next_cost < distance[i[0]]:
                distance[i[0]] = next_cost
                heapq.heappush(q, (next_cost, i[0]))
    return distance

ans = [0] * (n + 1)

for i in range(1, n + 1):
    ans[i] = dijkstra(i)[x] + dijkstra(x)[i]
    # dijkstra(i)[x] : i에서 x까지 이동
    # dijkstra(x)[i] : x에서 i까지 이동
print(max(ans))