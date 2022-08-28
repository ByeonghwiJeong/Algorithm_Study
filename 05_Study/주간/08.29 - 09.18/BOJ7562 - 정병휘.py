'''
https://www.acmicpc.net/problem/7562

<체스판 나이트의 이동>

입력)
- 1 : 테스트 케이스 T 
- 2 : 체스판의 한변의 길이 L [4 \ 300]
- 3 : 현재 칸 
- 4 : 목표 칸
'''
import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

T = int(input())

dr = (1, 2, 2, 1, -1, -2, -2, -1)
dc = (2, 1, -1, -2, -2, -1, 1, 2)

def valid_coord(r, c, l):
    return 0 <= r < l and 0 <= c < l

def bfs(r1, c1, d):
    visited[r1][c1] = True
    q = deque()
    q.append((r1, c1, d))
    while q:
        r, c, d = q.popleft()
        if r == er and c == ec:
            return d
        nd = d + 1
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if valid_coord(nr, nc, L):
                if not visited[nr][nc]:
                    q.append((nr, nc, nd))
                    visited[nr][nc] = True



for _ in range(T):
    L = int(input())
    visited = [[False] * L for _ in range(L)]
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    print(bfs(sr, sc, 0))