'''
https://www.acmicpc.net/problem/13913
제목: 숨바꼭질 4

- 수빈이는 동생을 찾기 위해 숨바꼭질을 하고 있다.
- 수빈이의 위치 N, 동생의 위치 K
- 수빈이는 1초 후에 X-1, X+1, 2*X로 이동할 수 있음

- 출력
    - 수빈이가 동생을 찾는 가장 빠른 시간
    - 수빈이가 동생을 찾는 경로

ex)
input
5 17
output
4
5 10 9 18 17
'''
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [-1] * 100001
parent = [-1] * 100001 # parent[x] = y : x의 부모는 y

def bfs():
    global cnt
    q = deque([(N, 0)])
    visited[N] = 0

    while q:
        x, t = q.popleft()
        if x == K:
            return x, t
        for nx in [x-1, x+1, 2*x]:
            if not (0 <= nx < 100001):
                continue
            if visited[nx] == -1: # not visited
                visited[nx] = t+1
                parent[nx] = x
                q.append((nx, t+1))

x, t = bfs()
path = []
while x != -1:
    path.append(x)
    x = parent[x]
print(t)
print(*path[::-1])





    