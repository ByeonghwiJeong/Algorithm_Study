'''
< 녹색 옷 입은 애가 젤다지? >
https://www.acmicpc.net/problem/4485
문제)
- NxN 크기의 동굴에서 (0, 0) -> (N-1, N-1) 디동한다.
- 동굴 각칸마다 도둑이 있다.
- 도둑의 크기만큼 소지금을 차감한다
- 잃을 수 밖에 없는 최소 금액은 ???
입력)
- 1     : 테스트 케이스의 N크기 ~ [2 \ 125]
    - 0 입력시 끝
- 2     : N x N 만큼 크기의 도둑

'''
import sys, heapq
input = sys.stdin.readline
INF = 10 ** 9
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dijkstra():
    q = []
    heapq.heappush(q, (a[0][0], 0, 0))
    visited[0][0] = a[0][0]
    while q:
        cost, r, c = heapq.heappop(q)
        if r == n - 1 and c == n - 1:
            return f"Problem {cnt}: {cost}"
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                ncost = cost + a[nr][nc]
                if ncost < visited[nr][nc]:
                    visited[nr][nc] = ncost
                    heapq.heappush(q, (ncost, nr, nc))

cnt = 1
while True:
    n = int(input())
    if n == 0: break
    a = [list(map(int,input().split())) for _ in range(n)]
    visited = [[INF] * n for _ in range(n)]
    print(dijkstra())
    cnt += 1
