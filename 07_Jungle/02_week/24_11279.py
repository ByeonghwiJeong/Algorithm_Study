'''
< 최대힙 >
https://www.acmicpc.net/problem/11279
문제)
- 자료구조 최대힙
1. 배열에 자연수 x를 넣는다.
2. 배열에 가장 큰 값을 출력하고, 그 값을 배열에 제거한다.
입력)
- 1     : 연산의 개수 N ~ [1 \ 100,000]
- 2     : x가 자연수인경우 x를 넣고, 0이라면 가장큰값을 넣고 출력
출력)
'''
import sys, heapq
input = sys.stdin.readline

hq = []
for _ in range(int(input())):
    x = int(input())
    if x: heapq.heappush(hq, (-x, x))
    else:
        if hq: print(heapq.heappop(hq)[1])
        else: print(0)