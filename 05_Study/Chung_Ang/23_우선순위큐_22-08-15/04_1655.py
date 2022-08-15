'''
1. 백준이 정수를 하나씩 외칠때마다
    - 동생은 말한 수중에서 중간값을 말해야한다.
2. 백준이 외친 수의 갯수가 짝수개라면 두수중에서 작은값을 말해야한다.

1 > (1)
5 > 1 5 > 1
2 > 


'''
import sys
import heapq
input = sys.stdin.readline

max_heap = []
min_heap = []
N = int(input())
mid = int(input())
print(mid)
for _ in range(N - 1):
    x = int(input())
    if x > mid:
        heapq.heappush(min_heap, x)
        if len(min_heap) > len(max_heap) + 1:
            heapq.heappush(max_heap, (-mid, mid))
            mid = heapq.heappop(min_heap)
    else:
        heapq.heappush(max_heap, (-x, x))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, mid)
            mid = heapq.heappop(max_heap)[1]
    print(mid)