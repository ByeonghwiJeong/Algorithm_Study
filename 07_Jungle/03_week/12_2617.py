'''
< 구슬 찾기 > 
https://www.acmicpc.net/problem/2617
문제) 
- 무게가 모두 다른 N개의 구슬이 있다.
- N은 홀수이며, 1 ~ N 으로 번호
- 무게가 전체의 중간 찾기 : 무게 순서로 (N + 1)/2 번째
- 양팔 저울
입력)
- 1     : 구슬개수N, 저울M
- 2[M]  : u, v ~~ u > v
출력)
'''
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heavy = [[] for _ in range(n + 1)]
light = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    heavy[u].append(v) # u > v ~ u가 무거움
    light[v].append(u) # v < u ~ v가 가벼움

def bfs(_list, x):
    cnt = 0
    visited[x] = 1
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for nxt in _list[x]:
            if visited[nxt]: continue
            visited[nxt] = 1
            q.append(nxt)
            cnt += 1
    return cnt    

ans = 0
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    big = bfs(heavy, i) # 무거운 구슬의 개수
    visited = [0] * (n + 1)
    small = bfs(light, i) # 가벼운 구슬의 개수
    # 중앙값인 구슬이 될 수 없는경우
    if big > (n - 1)//2  or small > (n - 1)//2: 
        ans += 1
print(ans)


