'''
https://www.acmicpc.net/problem/17071
제목: 숨바꼭질 5

- 수빈이는 동생을 찾기 위해 숨바꼭질을 하고 있다.
- 수빈이의 위치 N, 동생의 위치 K
- N ~ [0 \ 500,000], K ~ [0 \ 500,000]
- 수빈이는 1초 후에 X-1, X+1, 2*X로 이동할 수 있음
- 동생은 매초 이동
    - 이동은 가속이 붙는다.
    - 동생의 처음 위치는 K
    - 1초 후 K+1
    - 2초 후 K+1+2
    - 3초 후 K+1+2+3
    - ...
- 수빈이가 동생을 찾을 수 있는 가장 빠른 시간은?
    - input : 250000 499999
    - output : 1
- 수빈이가 동생을 찾을 수 없는 경우 -1 출력
    - input : 1 500000
    - output : -1
'''
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [[-1]*2 for _ in range(500001)]
# 


