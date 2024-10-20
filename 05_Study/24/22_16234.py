'''
https://www.acmicpc.net/problem/16234

제목 : 인구 이동
문제)
- N x N 크기의 땅이 있고, 땅은 1x1개의 칸으로 나누어져 있다. 
- 각각의 땅에는 나라가 하나씩 존재
- r행 c열에 있는 나라에는 A[r][c]명이 살고 있다.
- 인접한 나라 사이에는 국경선이 존재
- 모든 나라는 1x1 크기이기 때문에, 모든 국경선은 정사각형 형태

- 인구 이동 방법
    1. 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 국경선을 오늘 하루 동안 염
    2. 위 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작
    3. 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면 그 나라를 하루동안 연합이라고함
    4. 연합을 이루고 있는 각 칸의 인구수는 (연합 인구수) / (연합 칸의 개수) - 편의상 소수점은 버림
    5. 연합을 해체하고 모든 국경선을 닫음

- 인구이동이 몇일 동안 발생하는지? 구하는 프로그램 작성
    

입력)
- 1 : N ~ [1,  50], L, R ~ [1 / 100]
- 2 : N개의 줄에 각 나라의 인구수가 주어짐
'''
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

N, L, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

def dfs(r, c, visited):
    q = deque([(r, c)])
    visited[r][c] = 1
    union = [(r, c)] # 연합 좌표
    total_population = a[r][c]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(a[nr][nc] - a[r][c]) <= R: # 국경 열리는 기준
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    union.append((nr, nc))
                    total_population += a[nr][nc]

    if len(union) > 1:
        new_population = total_population // len(union)
        for r, c in union:
            a[r][c] = new_population
        return True # 인구 이동 O
    return False # 인구 이동 X


cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]
    flag = False # 인구 이동 여부

    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            flag |= dfs(i, j, visited) # 연합이 발생하면 True 

    if not flag: break
    cnt += 1
print(cnt)