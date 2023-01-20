'''
< 알파벳 >
https://www.acmicpc.net/problem/1987
문제)
- 세로R칸, 가로C칸으로 된 표 모양의 보드
- 보드 각칸에는 대문자 알파벳이 적혀있고, 좌축 상단칸(1, 1)에는 말이 놓여있다.
- 말은 상하좌우 이동
- 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 알파벳과 달라야 한다.
- 좌측 상단 부터 시작해서 말이 최대한 몇 칸을 지날 수 있는지 구하라
'''
from collections import deque
import sys
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

R, C = map(int, input().split())

a = [input().rstrip() for _ in range(R)]
visited = [[0] * C for _ in range(R)]

result = 0

# def dfs(r, c, s):
#     global result 
#     result = max(result, len(s))
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < R and 0 <= nc < C:
#             if not a[nr][nc] in s:
#                 dfs(nr, nc, s + a[nr][nc])

def dfs():
    global result
    q = []
    q.append((0, 0, a[0][0]))
    while q:
        r, c, s = q.pop()
        result = max(result, len(s))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if a[nr][nc] in s: continue
                q.append((nr, nc, s + a[nr][nc]))                    

dfs()
print(result)