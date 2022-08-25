'''
수빈이와 동생의 숨바꼭질
1초후 위치 X에서 
>>> X - 1 or X + 1 or X * 2
입력)
- 수빈위치N, 동생위치K ~ [0 \ 100,000]

'''
import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
visited = [False] * 100001 

def bfs(start, end):
    visited[start] = True
    q = deque()
    q.append((start, 0))
    while q:
        x, t = q.popleft()
        if x == end:
            return t
        _move = [x - 1, x + 1, x * 2]
        nt = t + 1
        for next in _move:
            if 0 <= next <= 100000:
                if not visited[next]:
                    visited[next] = True
                    q.append((next, nt))
print(bfs(N, K))