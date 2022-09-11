'''

'''
import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
_board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
# vistied 는 1을 0으로
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c):
    global sum
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if _board[nr][nc]:
                _board[nr][nc] = 0
                sum += 1
                dfs(nr, nc)

result = []

for i in range(N):
    for j in range(N):
        if _board[i][j]:
            _board[i][j] = 0
            sum = 1
            dfs(i, j)
            result.append(sum)

print(len(result))
print(*result, sep='\n')
'''
메모리 절약을 위해서 visited 선언하지않고 기존 _board활용
'''