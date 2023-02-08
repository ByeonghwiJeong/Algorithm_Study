'''
< 컴백홈 >
https://www.acmicpc.net/problem/1189
문제)
- 현재 위치 왼쪽 아래 [R-1][0]
- 목표 위치 오른쪽 위 [0][C-1]
- 한번방문한곳 다시 방문 X
- 거리가 K인 가짓수 구하라
- T는 못가는 부분
입력)
3 4 6
....
.T..
....
- 1     : R, C, K
- 2[R]  : 
'''
import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
visited = [[0] * C for _ in range(R)]
a = [input().rstrip() for _ in range(R)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def recur(r, c):
    if r == 0 and c == C-1:
        if visited[r][c] == K: return 1
        return 0
    ret = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if visited[nr][nc]: continue
            if a[nr][nc] == 'T': continue
            visited[nr][nc] = visited[r][c] + 1
            ret += recur(nr, nc)
            visited[nr][nc] = 0
    return ret

visited[R-1][0] = 1
print(recur(R-1, 0))

'''
재귀함수(r, c)
    목표 위치 도달
        조건❌ : return 1
        조건⭕️ : return 0
    ret = 0 선언
    4방향 탐색
        여러 조건 확인
        방문체크
        ret += 재귀함수(nr, nc)
        방문해제
    return ret
'''