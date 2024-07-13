'''
https://www.acmicpc.net/problem/14497
제목: 주난의 난

- N x M 크기의 격자판
    - 1: 친구
    - 0: 벽
    - *: 주난
    - #: 목적지
- 주난이는 4방향으로 갈수있으며 한 겹의 1친구들까지 이동가능

1 # 1 0 1 1 1
1 1 0 1 0 0 1
0 0 1 * 1 1 1
1 1 0 1 1 1 1
0 0 1 1 0 0 1

1 # 1 0 1 1 1
1 1 0 0 0 0 1
0 0 0 * 0 1 1
1 1 0 0 1 1 1
0 0 1 1 0 0 1

1 # 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 * 0 0 1
0 0 0 0 0 1 1
0 0 0 0 0 0 1

0 X 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 * 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0

3번의 이동으로 목적지에 도착함
- 주난이가 목적지에 도착하는데 걸리는 최소 시간 출력

입력예시)
5 7 # row, col
3 4 1 2
1#10111
1101001
001*111
1101111
0011001
'''
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
room = [list(input().strip()) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if visited[nx][ny] != -1:
                continue
            if room[nx][ny] == '0':
                visited[nx][ny] = visited[x][y] 
                q.appendleft((nx, ny))
            else: # 1 or * or #
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

bfs(x1 - 1, y1 - 1)
print(visited[x2 - 1][y2 - 1])