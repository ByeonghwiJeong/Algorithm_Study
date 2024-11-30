'''
https://www.acmicpc.net/problem/2075
제목: N번째 큰 수


'''
import sys, heapq
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    for v in map(int, input().split()):
        if len(heap) < N:
            heapq.heappush(heap, v)
        else:
            if heap[0] < v:
                heapq.heappop(heap)
                heapq.heappush(heap, v)

print(heap[0])
# N번째 큰수
"""

"""