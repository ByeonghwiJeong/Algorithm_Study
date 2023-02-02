'''
< 숨바꼭질 4 >
- https://www.acmicpc.net/problem/13913
문제)
- 수빈이 & 동생 숨바꼭질
- 수빈이는 현재 점 N ~ [0 \ 100,000]
- 동생은 점 K ~ [0 \ 100,000]
- 수빈이는 걷거나 순간이동 가능
    - 걷기 : 1초후 X+1 or X-1
    - 순간이동 : 1초후 2*X
- 수빈이가 동생을 찾는 가장 빠른 시간
입력)
- 1      : 수빈이 위치 N, 동생 위치 K
출력)
- 1      : 수빈이가 동생을 찾는 가장 빠른 시간
- 2      : 수빈이가 동생을 찾는 가장 빠른 경로
'''

from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
visited = [0] * 100001
prev = [0] * 100001

def bfs(s):
    visited[s] = 1
    q = deque()
    q.append((s))
    while q:
        x = q.popleft()
        if x == K:
            return visited[x]
        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= 100000:
                if not visited[nx]:
                    q.append((nx))
                    visited[nx] = visited[x] + 1
                    prev[nx] = x
ret = bfs(N)
v = []
v.append(K)
while K != N:
    K = prev[K]
    v.append(K)
print(ret - 1)
print(*v[::-1])



'''
⭐️⭐️⭐️이동 경로가 출력방법 prev ⭐️⭐️⭐️
1 => 4 => 9 => 11
prev[11] = 9
prev[9] = 4
prev[4] = 1

'''