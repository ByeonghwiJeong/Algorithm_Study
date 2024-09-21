'''
https://www.acmicpc.net/problem/1238
제목 : 파티

문제)
- N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있음
- N명의 학생이 X번 마을에 모여서 파티를 하려고 함
- 마을 사이에는 단방향 도로가 존재 (총 M개의 도로)
    - 도로마다 소모시간이 다름
- 이 학생들은 최단 시간에 오고 가기를 원함 (왕복)
- N명의 학생들 중 가장 오래 걸리는 학생은 ?

입력)
- 1    : N, M, X 
- 2 [M]: A, B, T (A -> B로 가는데 T시간 소요)
'''
import heapq
import sys
input = sys.stdin.readline

INF = sys.maxsize

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A].append((B, T))


def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, node = heapq.heappop(q)
        if distance[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            next_cost += cost
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(q, (next_cost, next_node))
    return distance

result = [0] * (N+1)

for i in range(1, N+1):
    result[i] = dijkstra(i)[X] + dijkstra(X)[i]

print(max(result))