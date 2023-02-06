"""
1. 아이디어
- MST 기본문제, 외우기
- 간선을 인접리스트에 집어넣기
- 힙에 시작점넣기
- 힙이 빌때까지 다음의 작업을 반복
    - 힙의 최소값 꺼내서, 해당 노드 방문 안했다면
            - 방분표시, 해당 비용 추가, 연결된 간선들 힙에 넣어주기
2. 시간복잡도
- MST : O(ElgE)
3. 자료구조
- 간선 저장 되는 인접리스트 : (무게, 노드번호)
- 힙 : (무게, 노드번호)
- 방문 여부 : bool[]
- MST 결과값 : int
<문제> 최소 스패닝 트리
https://www.acmicpc.net/problem/1197
"""
"""
<<< 핵심코드 >>>
import heapq
heap = [[0,1]] # 비용, 노드번호
while heap:
  w, next_node = heapq.heappop(heap)
  if  chk[next_node] == False:
    chk[next_node] = True
    rs += w
    for next_edge[1] == False:
      heapq.heappush(heap, next_edge)
"""
import heapq
from msvcrt import heapmin
import sys
input = sys.stdin.readline
# V정점 개수 , E간선 개수
V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]
chk = [False] * (V+1)
rs = 0

for i in range(E):
  a, b, c = map(int, input().split())
  edge[a].append([c, b]) # a와 b가 c가중치로 연결
  edge[b].append([c, a]) # b와 b가 c가중치로 연결
  # 양방향이라서 

heap = [[0, 1]] # 비용, 노드번결
print()
while heap:
  print("heap : ",heap)
  w, each_node = heapq.heappop(heap)
  print(f"w : {w} ,  each_node: {each_node}")
  print("heap : ",heap) 
  print()
  if chk[each_node] == False:
    chk[each_node] = True
    rs += w
    for next_edge in edge[each_node]:
      if chk[next_edge[1]] == False:
        heapq.heappush(heap, next_edge)

print(rs)