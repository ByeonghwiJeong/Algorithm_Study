'''
https://www.acmicpc.net/problem/12851
제목: 숨바꼭질 2

- 수빈이는 동생과 숨바꼭질을 하고 있다.
- 수빈이는 점 N ~ [0 \ 100,000]에 있음
- 동생은 점 K ~ [0 \ 100,000]에 있음
- 수빈이의 위치가 X일 때 1초 후에 X-1, X+1, 2*X로 이동할 수 있음
- 수빈이가 동생을 찾을 수 있는 가장 빠른 시간은?
- 가장 빠른 시간으로 찾는 방법이 몇 가지인지 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [-1] * 100001
cnt = [0] * 100001

def bfs():
    global cnt
    q = deque([(N, 0)])
    visited[N] = 0
    cnt[N] = 1
    while q:
        x, t = q.popleft()
        if x == K:
            return t, cnt[x]
        for nx in [x-1, x+1, 2*x]:
            if not (0 <= nx < 100001):
                continue
            if visited[nx] == -1: # not visited
                visited[nx] = t+1
                cnt[nx] += cnt[x]
                q.append((nx, t+1))
            elif visited[nx] == t+1: # visited and same time
                cnt[nx] += cnt[x]

t, c = bfs()
print(t)
print(c)




    