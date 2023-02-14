'''
< 거의 최단 경로 >
https://www.acmicpc.net/problem/5719
문제)
- 네비게이션 : 출발 ~ 도착 최단 경로 검색
    - 교통상황을 고려하지않을 경우 정체 겸험
- 상근이의 네비게이션
    - 항상 거의 최단 경로를 찾아줌
    - 절대로 최단경로를 찾아주지 않는다.
- 거의 최단 경로란 ???
    - 최단 경로에 포함되지 않는 도로로만 이루어진 경로 중 가장 짧은것
입력)
- 1     :  장소의 수 N ~ [2 \ 500], 도로의 수 M ~ [1 \ 10^4]
    - 장소는 0부터 N-1번까지 번호로 할당
    - N과M이 0인경우 종료
- 2     : 시작점 S, 도착점 D ~ [0 \ N)
    - S != D 
- 3[M]  : U, V, P
    - U에서 V로 가는 도로는 최대 한개, 길이는 P
    - U > V, V > U 도로는 다르다 : 단방향
출력)
- 1     : 
'''
import sys, heapq
from collections import deque
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra():
    distance = [INF] * (N + 1)
    pq = []
    heapq.heappush(pq, (0, S))
    distance[S] = 0
    while pq:
        cost, now = heapq.heappop(pq)
        if distance[now] < cost: continue
        for i, nxt in enumerate(a[now]):
            if nxt == -1: continue
            next_cost = cost + nxt
            if distance[i] > next_cost:
                distance[i] = next_cost
                heapq.heappush(pq, (next_cost, i))
    return distance

def eraseEdge():
    q = deque()
    q.append(E)
    while q:
        x = q.popleft()
        for i in range(N):
            if distances[x] == distances[i] + a[i][x] and a[i][x] != -1:
                a[i][x] = -1
                q.append(i)
    

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0: break
    S, E = map(int, input().split())
    a = [[-1] * N for _ in range(N)]
    for _ in range(M):
        U, V, P = map(int, input().split())
        a[U][V] = P
    distances = dijkstra()
    eraseEdge()
    distances = dijkstra()
    print(-1 if distances[E] == INF else distances[E])


'''
간선을 직접적으로 지울수는 없고 cost(거리)를 -1로 표기!!!
기본적인 다익스트라 문제
'''