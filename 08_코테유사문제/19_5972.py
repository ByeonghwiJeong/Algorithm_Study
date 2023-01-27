'''
< 택배배송 >
https://www.acmicpc.net/problem/5972
문제)
- 현서는 찬홍이에게 택배를 배달해야한다.
- 가는길에 평화롭게가려면 만나는 모든 소들에게 여물을 줘야함
- N ~ [1 \ 50,000] 개의 헛간
- 소들의 길인 M ~ [1 \ 50,000] 개의 양방향 길이 그려져 있다.
- 각각의 길은 C_i ~ [0, 1000] 마리의 소가 있습니다.
- 소들의 길 A_i(헛간) B_i(헛간) C_i
- 1번 헛간 >>> N번 헛간
입력)
- 1     : N, M
- 2[M]  : 헛간1, 헛간2, 비용(마리)
출력)
- 최소 비용


'''
import sys, heapq
input = sys.stdin.readline

INF = 10 ** 9
N, M = map(int, input().split())
graph = [[] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    st, en, cost = map(int, input().split())
    graph[st].append((en, cost))
    graph[en].append((st, cost))

def dijkstra(start_node):
    distance = [INF] * (N + 1)
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

print(dijkstra(1)[N])
