'''
< 인구 이동 > 
https://www.acmicpc.net/problem/16234
문제 : BFS)
- N x N크기의 땅이 있고, 땅은 1 x 1개의 칸으로 나누어져 있다.
- 각각의 땅에는 나라가 하나씩 존재 
- r행 c열에 있는 나라에는 A[r][c]명이 살고 있다.
- < 인구 이동 규칙 > 인구 이동이 시작 
    - 국경선을 공유하는 두 나라의 인구 차이가 L명이상, R명이하 두 나라가 공유하는 국경 OPEN
    - 국경OPEN시 인구이동 Start
    - 국경열려있으면 연합 (하루동안)
    - 연합을 이루고 있는 각 칸의 인구수 = 연합 인구수 / 연합을 이루고 있는 칸의 개수
    - 연합을 해체하고, 모든 국경선 CLOSE
- 인구이동이 몇번 발생하는지 구하라
입력)
- 1     :  N, L, R (1 <= N <= 50, 1 <= L <= R <= 100)
- 2     :  A[1][1] ~ A[N][N] (0 <= A[r][c] <= 100)
- 인구이동이 발생하는 횟수가 2,000번 보다 작거나 같은 입력만 주어진다.
출력)
- 인구이동이 몇번 발생하는지 출력
'''
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N, L, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

def dfs(r, c):
    global v, sum
    q = [(r, c)]
    while q:
        r, c = q.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N: 
                if visited[nr][nc]: continue
                diff = abs(a[nr][nc] - a[r][c])
                if L <= diff <= R:
                    visited[nr][nc] = 1
                    v.append((nr, nc))
                    sum += a[nr][nc]
                    q.append((nr, nc))


cnt = 0
while True:
    flag = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            v = []
            visited[i][j] = 1
            v.append((i, j))
            sum = a[i][j]
            dfs(i, j)
            if len(v) == 1: continue
            for r, c in v:
                a[r][c] = sum // len(v)
                flag = 1
    # print(*a, sep='\n', end='\n\n')
    if not flag: break
    cnt += 1
print(cnt)