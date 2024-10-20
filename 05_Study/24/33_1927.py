'''
https://www.acmicpc.net/problem/1927
제목 : 최소 힙

문제)
- 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성
1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.


'''

import sys
import heapq
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    x = int(input())
    if x: # push
        heapq.heappush(heap, x)
    else: # pop
        print(heapq.heappop(heap) if heap else 0)

    
