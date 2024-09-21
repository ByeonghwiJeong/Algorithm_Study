'''
https://www.acmicpc.net/problem/4485
제목 : 녹색 옷 입은 애가 젤다지?

문제)
- NxN 크기의 동굴에서 (0, 0) -> (N-1, N-1) 이동
- 각 칸마다 도둑이 있음 (도둑의 크기만큼 소지금 차감)
- 잃을 수 밖에 없는 최소 금액은?

입력)
- 1     : 테스트 케이스의 N크기 ~ [2 \ 125] (0 입력시 끝)
- 2     : N x N 만큼 크기의 도둑    

'''
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dijkstra():
    hq = []
    heapq.heappush(hq, (a[0][0], 0, 0))
    visited[0][0] = a[0][0]
    while hq:
        cost, r, c = heapq.heappop(hq)
        if r == N - 1 and c == N - 1:
            return f"Problem {cnt}: {cost}"
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                ncost = cost + a[nr][nc]
                if ncost < visited[nr][nc]:
                    visited[nr][nc] = ncost
                    heapq.heappush(hq, (ncost, nr, nc))

cnt = 1
while True:
    N = int(input())
    if N == 0: break
    a = [list(map(int,input().split())) for _ in range(N)]
    visited = [[INF] * N for _ in range(N)]
    print(dijkstra())
    cnt += 1