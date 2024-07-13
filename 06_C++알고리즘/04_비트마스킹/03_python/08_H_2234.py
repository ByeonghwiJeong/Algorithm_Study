'''
https://www.acmicpc.net/problem/2234
제목: 성곽

문제
- M x N ~ [1, 50] 크기의 성곽
- 성곽은 방이 있는 곳과 벽이 있는 곳으로 이루어져 있다.
- 성의 지도를 입력받아서 다음을 출력하라
    1. 방의 개수
    2. 가장 넓은 방의 넓이
    3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
입력)
- 첫째줄: N, M (1<=M, N<=50)
- 둘째줄~M+1줄: N개의 정수 (각각의 정수는 0~15) -> 방의 정보
    - 1: 서쪽 벽
    - 2: 북쪽 벽
    - 4: 동쪽 벽
    - 8: 남쪽 벽
'''
import sys
from collections import deque
input = sys.stdin.readline

# 서, 북, 동, 남 ㅜㅜ
dr = (0, -1, 0, 1)
dc = (-1, 0, 1, 0)
N, M = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1
    cnt = 1 # 방의 크기
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < M and 0 <= nc < N): # 범위를 벗어난 경우
                continue
            if visited[nr][nc]: # 이미 방문한 경우
                continue
            if castle[r][c] & (1 << i): # 벽이 있는 경우
                continue
            q.append((nr, nc))
            visited[nr][nc] = 1
            cnt += 1
    return cnt

room_cnt = 0
max_room_size = 0
max_room_size_with_break = 0

for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue
        room_cnt += 1
        max_room_size = max(max_room_size, bfs(i, j))

# 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
for i in range(M):
    for j in range(N):
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if not (0 <= nr < M and 0 <= nc < N): # 범위를 벗어난 경우
                continue
            if castle[i][j] & (1 << k): # 벽이 있는 경우
                visited = [[0] * N for _ in range(M)]
                castle[i][j] -= (1 << k) # 벽을 제거
                max_room_size_with_break = max(max_room_size_with_break, bfs(i, j))
                castle[i][j] += (1 << k) # 원상복구


print(room_cnt)
print(max_room_size)
print(max_room_size_with_break)


