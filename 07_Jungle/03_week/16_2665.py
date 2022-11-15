'''
< 미로만들기 > 
https://www.acmicpc.net/problem/2665
문제) 다익스트라
- n x n 바둑판 : 흰 or 검
입력)
- 1     : 한줄의 방의 수 N [1 \ 50]
- 2[N]  : 0은 검은방 1은 흰방 : 검은방은 벽
출력)
- 
'''
import sys, heapq
input = sys.stdin.readline
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
n = int(input())
visited = [[0] * n for _ in range(n)]
board = [list(map(int, input().rstrip())) for _ in range(n)]

def dijkstra(r, c):
    hq = [(0, r, c)]
    visited[r][c] = 1
    while hq:
        w, r, c = heapq.heappop(hq)
        if r == n - 1 and c == n - 1:
            return w
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if visited[nr][nc]: continue
                visited[nr][nc] = 1
                if board[nr][nc]: heapq.heappush(hq, (w, nr, nc))
                else: heapq.heappush(hq, (w + 1, nr, nc))

print(dijkstra(0, 0))