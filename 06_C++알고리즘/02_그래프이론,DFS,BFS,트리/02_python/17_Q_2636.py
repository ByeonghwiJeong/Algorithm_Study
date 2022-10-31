import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
cnt = 0

def dfs(r, c):
    global visited, l
    visited[r][c] = 1
    if a[r][c]: 
        l.append((r, c))
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if visited[nr][nc]: continue
            dfs(nr, nc)
    return

while True:
    cnt2 = 0 # 직전 치즈 갯수
    visited = [[0] * m for _ in range(n)]
    l = []
    dfs(0, 0)
    for i in l:
        cnt2 += 1
        a[i[0]][i[1]] = 0
    flag = 0
    for i in range(n):
        for j in range(m):
            if a[i][j]: flag = 1
    cnt += 1 # 전체 시간
    if not flag: break # 1이 하나도없을때 break
print(cnt)
print(cnt2)