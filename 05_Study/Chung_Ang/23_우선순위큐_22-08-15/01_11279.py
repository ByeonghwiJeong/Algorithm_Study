'''
<< 최댓값 힙 >>
1. 배열에 자연수 x
2. 배열에서 가장 큰값을 출력, 그값을 제거

파이썬은 최소힙으로 구현
'''

import sys
import heapq
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(heap, (-x, x))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except IndexError:
            print(0)
# heapq.heappush(heap, 6)
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 4)
# heapq.heappush(heap, 8)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 2)

# print(heap)

# print(heapq.heappop(heap))

# print(heap)

# print(heapq.heappop(heap))

# print(heap)

# print(heapq.heappop(heap))

# print(heap)

# print(heapq.heappop(heap))

# print(heap)