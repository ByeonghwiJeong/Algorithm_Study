import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
  n = int(input())
  if n:
    hq.heappush(pq, (abs(n), n))
  else:
    # print(hq.heappop(pq)[1] if pq else print(0))
    if pq:
      print(hq.heappop(pq)[1])
    else:
      print(0)


