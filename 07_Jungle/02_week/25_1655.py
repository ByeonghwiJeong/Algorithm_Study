'''
< 가운데를 말해요 >
https://www.acmicpc.net/problem/1655
문제)
- 짝수개라면 중간에 있는 두수중 작은값
    >>> min_hq에 원소가 더 많다.
    1   : min_hq가 max_hq보다 한개 원소 많은경우
    2   : 원소수 같은 경우
입력)
- 
출력)
-
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline


max_hq = []
min_hq = []
N = int(input())
mid = int(input())
print(mid)
for _ in range(N - 1):
    n = int(input())
    if n >= mid:
        heappush(min_hq, n)
        if len(min_hq) > len(max_hq) + 1:
            heappush(max_hq, (-mid, mid))
            mid = heappop(min_hq)
    else:
        heappush(max_hq, (-n, n))
        if len(max_hq) > len(min_hq):
            heappush(min_hq, mid)
            mid = heappop(max_hq)[1]
    print(mid)


