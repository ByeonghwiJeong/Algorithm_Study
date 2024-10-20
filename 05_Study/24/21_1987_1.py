'''
https://www.acmicpc.net/problem/1987

제목 : 알파벳

문제)
- 세로 R칸, 가로 C칸
- 각 칸에는 대붐낮 알파벳이 하나씩 적혀 있음
- 말은 상하좌우 이동가능
- 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야한다.(같은 알파벳 지나갈수 없음)
- 왼쪽 위에서 출발

입력)
- 1 : R C 가 빈칸을 사이에 두고 주어진다.
- 2 :[R lines] C개의 알파벳

ex)
2 4
CAAB
ADCB
'''
# TODO : 시간 초과!!! --> 비트 마스킹 활용?

import sys
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c, cnt, visited):
    global ret
    ret = max(ret, cnt)
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if a[nr][nc] not in visited:
                visited.add(a[nr][nc])
                dfs(nr, nc, cnt + 1, visited)
                visited.remove(a[nr][nc])

R, C = map(int, input().split())
a = [input().rstrip() for _ in range(R)]

visited = set()
visited.add(a[0][0])
ret = 0

dfs(0, 0, 1, visited)

print(ret)
