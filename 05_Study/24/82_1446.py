"""
https://www.acmicpc.net/problem/1446
제목: 지름길

문제)
- 보통 차를 타고 D[km]거리의 고속도로로 이동하려고 한다.
- 일방 통행인 지름길을 알게됐다.
- 고속도로는 역주행 불가능
- 세준이가 운전하는 거리의 최솟값?

입력 예시)
5 150       - 지름길 개수 N, 고속도로 길이 D ,  N~[1, 12] D[1, 10_000]
0 50 10     - [N줄] 시작위치, 도착위치, 지름길 길이
0 50 20
50 100 10
100 151 10
110 140 90
"""
import sys, heapq
input = sys.stdin.readline

N, D = map(int, input().split())
graphs = [[] for _ in range(D+1)]
INF = 1e9
distance = [INF] * (D+1)

for _ in range(N):
    s, e, l = map(int, input().split())
    if e > D:
        continue
    graphs[s].append((e, l)) # 지름길

for i in range(D):
    graphs[i].append((i+1, 1)) # 기본 도로

# 다익스트라 (dijkstra)
def dijkstra():
    q = [] # 우선순위 큐 (비용, 위치)
    heapq.heappush(q, (0, 0))
    distance[0] = 0 # 시작점 비용 0

    while q:
        cost, pos = heapq.heappop(q)
        if distance[pos] < cost:
            continue
        for i in graphs[pos]:
            next_pos, next_add_cost = i # 다음 위치, 다음 위치 비용
            next_cost = cost + next_add_cost
            if next_cost < distance[next_pos]:
                distance[next_pos] = next_cost
                heapq.heappush(q, (next_cost, next_pos))

dijkstra()
print(distance[D])



            

