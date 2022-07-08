import heapq as hq
import sys
input = sys.stdin.readline

min_heap = [] # 양수
max_heap = [] # 음수 
N = int(input())

for _ in range(N):
  x = int(input())
  if x:
    if x > 0:
      hq.heappush(min_heap, x)
    else:
      hq.heappush(max_heap, -x)
  else: # x = 0 인경우
    if min_heap:
      if max_heap: # 절대값이 작은 쪽 peak!! 
        if min_heap[0] < abs(max_heap[0]):
          print(hq.heappop(min_heap))
        else:
          print(-hq.heappop(max_heap))
      else:
        print(hq.heappop(min_heap))

    else:
      if max_heap:
        print(-hq.heappop(max_heap))
      else: # 둘다 빈경우
        print(0)