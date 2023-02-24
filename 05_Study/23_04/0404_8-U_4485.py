'''
< 녹색 옷 입은 애가 젤다지? >
https://www.acmicpc.net/problem/4485
- 화폐단위 루피
- '도둑루피' : 소지한 루피 감소
- 시작 포인트 : (0,0) - 제일 왼쪽 위
- 도착 포인트 : (N-1, N-1) - 제일 오른쪽 아래
- 동굴의 각 칸마다 도둑루피가 있다.
- 잃을 수 밖에 없는 루피의 최솟값
입력)
- 1         : 동굴의 크기 N
    - 0     : 종료
- 2[N]      : 동굴의 각 칸마다 도둑루피의 양
'''
import sys
from heapq import heappush, heappop
INF = 10 ** 9
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dijkstra():
    hq = []
    heappush(hq, (a[0][0], 0, 0))
    visited[0][0] = a[0][0]
    while hq:
        cost, r, c = heappop(hq)
        if r == N - 1 and c == N - 1: return cost
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                ncost = cost + a[nr][nc]
                if ncost < visited[nr][nc]:
                    visited[nr][nc] = ncost
                    heappush(hq, (ncost, nr, nc))

cnt =  1
while True:
    N = int(input())
    if N == 0: break
    a = [list(map(int, input().split())) for _ in range(N)]
    visited = [[INF for _ in range(N)] for _ in range(N)]
    print(f'Problem {cnt}: {dijkstra()}')
    cnt += 1