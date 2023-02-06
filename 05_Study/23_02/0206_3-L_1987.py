'''
< 알파벳 >
https://www.acmicpc.net/problem/1987
문제)
- R x C 보드
- 각칸에는 대문자 알파벳 한개
- 좌측상단칸 (1행 1열) 시작
- 같은 알파벳 두번 X
- 말이 최대 몇칸 지날수 있는지??? (1, 1)포함
입력)
- 1     : R, C
- 2[R]  : C개의 알파벳 (띄어쓰기X)
'''
import sys
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

R, C = map(int, input().split())
a = [input().rstrip() for _ in range(R)]
visited = [0] * 26
ret = 0 
def dfs(r, c, cnt):
    global ret
    ret = max(ret, cnt)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            v = ord(a[nr][nc]) - ord('A')
            if visited[v]: continue
            visited[v] = 1
            dfs(nr, nc, cnt + 1)
            visited[v] = 0

visited[ord(a[0][0])-ord('A')] = 1
dfs(0, 0, 1)
print(ret)
'''
dfs함수 호출전 방문처리!!!
'''