'''
< 인구 이동 >
https://www.acmicpc.net/problem/16234
문제)
- NxN땅, 각땅에는 사람수 표기
- < 인구 이동이 시작되는 날 >
    - 1. 국경선 공유하는 두 나라의 인구 차이가 L명이상 R명이하면\
        하루동안 국경 OPEN
    - 2. 위 조건에 의해 국경을 모두 열었다면, 인구 이동 시작
    - 3. 국경 열려있으면 하루동안 "연합"
    - 4. 연합 각 칸의 인구수: (연합의 인구수)/(연합을 이루고 있는 카의 개수)
    - 5. 연합을 해체하고, 모든 국경선을 닫는다.
- 몇일 동안 인구 이동이 발생하는가??
'''
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, L, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c):
    global v, sum
    q = [(r, c)]
    while q:
        r, c = q.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if visited[nr][nc]: continue
                diff = abs(a[nr][nc] - a[r][c])
                if L <= diff <= R:
                    visited[nr][nc] = 1
                    sum += a[nr][nc]
                    v.append((nr, nc))
                    q.append((nr, nc))
                    

cnt = 0
while True:
    flag = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]: continue
            v = []
            visited[i][j] = 1
            v.append((i, j))
            sum = a[i][j]
            dfs(i, j)
            if len(v) == 1: continue
            for r, c in v:
                a[r][c] = sum//len(v)
                flag = 1
    # print(*a, sep='\n', end='\n\n')
    if not flag: break
    cnt += 1

print(cnt)