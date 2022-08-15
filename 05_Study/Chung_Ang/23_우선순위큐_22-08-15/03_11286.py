'''
<< 절댓값 힙 >>

'''
import sys
import heapq
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except IndexError:
            print(0)
    
