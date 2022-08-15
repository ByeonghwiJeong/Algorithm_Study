# << 절댓값 힙 >>
import sys
import heapq
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(heap, x)
    else:
        try:
            print(heapq.heappop(heap))
        except IndexError:
            print(0)
