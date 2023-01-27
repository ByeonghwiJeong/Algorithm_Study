'''
< 지름길 >
https://www.acmicpc.net/problem/1446
문제)
- 매일, 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다.
- 지름길 존재 ( 단반향 그래프 )
- 거리의 최솟값
입력)
- 1     : 지름길의 개수 N, 고속도로의 길이 D
- 2[N]  : 지름길의 시작 위치, 도착 위치, 지름길 길이   
'''
import sys, heapq
input = sys.stdin.readline

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
INF = 1e9

def dijkstra(start):
    distance = [INF] * (D + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost: continue
        for i in graph[now]:
            next_cost = i[1] + cost
            try:
                if next_cost < distance[i[0]]:
                    distance[i[0]] = next_cost
                    heapq.heappush(q, (next_cost, i[0]))
            except:
                print(i[0])
                exit(0)
    return distance

for i in range(D):
    graph[i].append((i+1, 1))
    # i=0 : 0 > 1
    # i=D-1 : D-1 > D
for _ in range(N):
    s, e, l = map(int, input().split())
    if e > D: continue
    graph[s].append((e, l))

print(dijkstra(0)[D])


