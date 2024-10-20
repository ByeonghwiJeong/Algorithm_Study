'''
https://www.acmicpc.net/problem/24042
제목 : 횡단보도

문제)
- 사람이 지나갈 수 있는 N개의 지역이 있다 (1번 ~ N번)
- 횡단보도에 파란불이 들어오는 순서를 알고 있음
- 횡단보도의 주기는 총 M분이며 1분마다 신호가 바뀜
- 각 주기의 1 + i 번째 신호
    - N * M + i 분에 시작해서 1분동안 A지역과 B지역을 잇는 횡단보도에 파란불
    - 다른 모든 횡단보도에는 빨간불이 들어옴
- 한 주기동안 같은 횡단보도에 파란불이 여러번 들어올 수 있음
- 횡단보도를 건너는데 1분이 걸림
- 횡단보도와 신호의 정보가 주어질 때, 시간 0분에서 시작해서
    - 1번 지역 ~ N번 지역까지가는 최소 시간을 구하는 프로그램을 작성

입력)
- 1    : 지역의 수 N, 횡단보도의 주기 M
- 2 [M]: M개의 줄중 1 + i번째 줄에는 i, M +i, 2M + i, ... , N * M + i 분에 시작해서
         1분동안 파란불이 들어오는 횡단보도의 두 끝점 Ai, Bi가 주어짐 
'''

'''
여러 개의 양방향 경로가 존재하는 그래프
1번 노드에서 N번 노드로 가는 최소 시간을 구하는 문제
1+i번째 줄에 나오는 A에서 B로 가는 횡단보도는 1 + i분에 이용가능 A-B 간선이 1+i만큼의 비용을 가짐
'''
import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((i, b)) # i분에 a에서 b로 가는 횡단보도
    graph[b].append((i, a)) # i분에 b에서 a로 가는 횡단보도

INF = sys.maxsize


distance = [INF] * (N+1)
distance[1] = 0 # 1번 노드에서 시작 (시간 0분)

# 우선순위 큐를 이용한 다익스트라
q = []
heapq.heappush(q, (0, 1)) # 1번 노드에서 시작 (현재시각, 현재노드번호)

while q:
    time, node = heapq.heappop(q) # 현재 가장 빠른 시간에 도착한 노드와 시간
    if distance[node] < time: # 이미 더 빠른 경우 무시
        continue
    for cost, next_node in graph[node]: # 현재 노드의 횡단보도 정보 확인

        # 현재 시간에서 이 횡단 보도를 이용할 수 있는 가장 빠른 시간
        tmp = (time - cost) // M
        if (time - cost) % M: # 나머지가 있으면 다음 주기로 넘어가야함
            tmp += 1
        next_time = cost + M * tmp + 1 # 다음 횡단보도를 이용할 수 있는 시간 (+1 이동시간)

        if distance[next_node] > next_time:
            distance[next_node] = next_time
            heapq.heappush(q, (next_time, next_node))

print(distance[N])