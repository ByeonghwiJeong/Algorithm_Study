'''
위치 N보다 큰값(1000)을 곱하고 더하면 2차원을 1차워로 바꿀 수 있다.
꺼낼때는 나누고 몫과 나머지를 이용하면 된다.
'''
import sys
from heapq import heappush, heappop
INF = 10 ** 9
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dijkstra():
    hq = []
    heappush(hq, (a[0][0], 0))
    visited[0][0] = a[0][0]
    while hq:
        cost, p = heappop(hq)
        r, c = p // 1000, p % 1000
        if r == N - 1 and c == N - 1: return cost
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                ncost = cost + a[nr][nc]
                if ncost < visited[nr][nc]:
                    visited[nr][nc] = ncost
                    heappush(hq, (ncost, nr * 1000 + nc))

cnt =  1
while True:
    N = int(input())
    if N == 0: break
    a = [list(map(int, input().split())) for _ in range(N)]
    visited = [[INF for _ in range(N)] for _ in range(N)]
    print(f'Problem {cnt}: {dijkstra()}')
    cnt += 1