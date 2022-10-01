'''
세로R칸 가로C칸으로 된 표 모양의 보드가 있다.
(0, 0)에서 말이 놓여있다
상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있다.
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 알파벳과는 달라야한다.
'''
R, C = map(int, input().split())
alpa = [input().rstrip() for _ in range(R)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

result = 0

def dfs(r, c, s):
    global result 
    result = max(result, len(s))
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if not alpa[nr][nc] in s:
               dfs(nr, nc, s+alpa[nr][nc])

dfs(0, 0, alpa[0][0])
print(result)
'''
시간초과가 나서 PYPY를 사용했다 골드이지만 골드 같지 않은 문제였다.
'''