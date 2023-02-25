'''
< 오민식의 고민 >
https://www.acmicpc.net/problem/1219
문제)
- 오민식은 물건을 최대한 많이 팔아서 최대 이윤을 얻으려고 한다.
- N개의 도시가 있다. (0번 도시부터 N-1번 도시까지)
- 오민식의 여행은 A도시에서 B도시에서 끝나낟.
- 도시 이동시 비용이 들고, 도시에서 물건을 팔면 이익이 된다.
- 오민식은 도착 도시에 도착할 때, 가지고 있는 돈의 액수를 최대로 하려고 한다.
- 버는 돈보다 쓰는돈이 많다면 가지고 있는 돈의 액수가 음수가 될 수 있다.
입력)
- 1      : 도시의 수 N, 시작 도시, 도착 도시, 교통 수단의 개수 M
- 2[M]   : 교통 수단의 정보
    - 시작, 끝, 가격
- 3      : 오민식이 각 도시에서 벌 수 있는 돈의 최댓값
    - 0번 도시부터 N-1번 도시까지
출력)
- 1      : 도착 도시에 도착했을 때, 가지고 있는 돈의 액수의 최댓값
    - 도착 도시에 도착하는것이 불가능할 때는 "gg"를 출력
    - 도착 도시에 도착했을 때 돈을 무한히 많이 가지고 잇을 수 있다면 "Gee"를 출력
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

N, S, E, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
costs = list(map(int, input().split()))
dist = [-INF] * (N + 1)

def bellmon_ford():
    global dist
    dist[S] = costs[S]
    # 전체 N-1번의 라운드(round)를 반복
    for i in range(N):
        # 매 반복마다 "모든 간선"을 확인하며
        for j in range(N):
            cur_node = j
            for next_node, edge_cost in graph[cur_node]:
                # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if dist[cur_node] == -INF: continue
                if dist[next_node] < dist[cur_node] + costs[next_node] - edge_cost:
                    dist[next_node] = dist[cur_node] + costs[next_node] - edge_cost
                    # N번째 라운드에서도 값이 갱신된다면 양의 사이클이 존재한다.
                    if i == N-1:
                        return cur_node
    return None

cycle_start = bellmon_ford()
flag = False
if cycle_start:
    visited = [False] * N
    q = [cycle_start]
    visited[cycle_start] = True
    while q:
        cur_node = q.pop()
        for next_node, _ in graph[cur_node]:
            if next_node == E:
                flag = True
                break
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
        if flag: break
#     if flag:
#         print("Gee")
#     else:
#         print("gg")
# else:
#     if dist[E] == -INF:
#         print("gg")
#     else:
#         print(dist[E])
if dist[E] == -INF:
    print("gg")
elif flag:
    print("Gee")
else:
    print(dist[E])

'''

- 양의 사이클이 존재하는 경우, 돈을 무한히 많이 가질 수 있다.

'''