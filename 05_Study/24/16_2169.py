'''
https://www.acmicpc.net/problem/2169
제목 : 로봇 조종하기

문제)
- N x M 지도
- 지형의 고저차 특성상 로봇은 왼쪽, 오른쪽, 아래쪽으로 이동 (위쪽으로는 이동 불가)
- 로봇은 (1, 1)에서 시작 ~ 왼쪽, 위
- 목적지는 (N, M)
- 각각의 지역은 탐사 가치가 있음
- 탐사한 지역들의 가치의 합이 최대인 값


입력)
5 5
10 25 7 8 13
68 24 -78 63 32
12 -69 100 -29 -25
-16 -22 -57 -33 99
7 -76 -11 77 15
출력)
319
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

value_board = [list(map(int, input().split())) for _ in range(N)]

dp = [[float('-inf')]*M for _ in range(N)]

dp[0][0] = value_board[0][0]

# 첫번째 열 (왼쪽 -> 오른쪽)    
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + value_board[0][i]

for i in range(1, N):
    # 왼쪽에서 오른쪽
    left_to_right = [float('-inf')]*M
    left_to_right[0] = dp[i-1][0] + value_board[i][0]
    for j in range(1, M):
        left_to_right[j] = max(left_to_right[j-1], dp[i-1][j]) + value_board[i][j]

    # 오른쪽에서 왼쪽
    right_to_left = [float('-inf')]*M
    right_to_left[-1] = dp[i-1][-1] + value_board[i][-1]
    for j in range(M-2, -1, -1):
        right_to_left[j] = max(right_to_left[j+1], dp[i-1][j]) + value_board[i][j]

    # 최종 갱신
    for j in range(M):
        dp[i][j] = max(left_to_right[j], right_to_left[j])


print(dp[N-1][M-1])