'''
https://www.acmicpc.net/problem/17484
제목 : 진우의 달 여행 (Small)

문제)
- 지구와 달 사이에 N X M 행렬로 나타낼 수 있다
- 각 원소의 값은 우주선이 그 지점을 지날 때 소모되는 연료의 양
- 지구 -> 달 : 이동방향 아래, 아래 오른쪽, 아래 왼쪽
- 같은 방향으로 연속해서 이동할 수 없다
- 최소 연료 소모량을 구하라


입력)
- 1		: N, M ~ [2, 6]
- 2		: N X M 행렬

6 4
5 8 5 1
3 5 8 4
9 77 65 5
2 1 5 2
5 98 1 5
4 95 67 58

29
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 방향 벡터 (아래, 아래 오른쪽, 아래 왼쪽)
dr = [1, 1, 1]
dc = [0, 1, -1]

dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]



for i in range(1, N):
    for j in range(M):
        for k in range(3): # 현재 이동 방향
            for pd in range(3): # 이전 이동 방향
                if d == pd: continue # 같은 방향으로 이동할 수 없음
                pr, pc = i + dr[pd], j + dc[pd]
                if 0 <= nr < N and 0 <= nc < M:
                    dp[i][j][k] = min(dp[i][j][k], dp[nr][nc][pd] + board[i][j])

print(min(dp[-1][-1]))
        
        