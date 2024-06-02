"""
https://www.acmicpc.net/problem/17070
백준 17070. 파이프 옮기기 1, G5
- N x N 크기
- 대각선만 조심하면됨
- 1벽, 0은 빈칸
- 파이프는 3가지 방향으로 이동 가능
    - 가로 : 오른쪽, 대각선 : 오른쪽 아래, 세로 : 아래
- 파이프는 빈 칸만 이동 가능
"""


N = int(input().strip())
a = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
dp = [[[0, 0, 0] for _ in range(N + 2)] for _ in range(N + 2)] # 가로, 대각선, 세로

for i in range(1, N + 1):
    row = list(map(int, input().strip().split()))
    for j in range(1, N + 1):
        a[i][j] = row[j - 1] # 경계 조건때문에 한 칸씩 밀어줌

def check(y, x, d):
    if d == 0 or d == 2: # 가로, 세로
        if not a[y][x]: # 빈칸인 경우
            return True
    elif d == 1: # 대각선
        if a[y][x] == 0 and a[y - 1][x] == 0 and a[y][x - 1] == 0:
            # 현재위치, 위, 왼쪽이 빈칸인 경우 
            return True
    return False

dp[1][2][0] = 1 # 초기값 (1, 2) 가로 파이프

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if check(i, j + 1, 0): # 가로 OK
            dp[i][j + 1][0] += dp[i][j][0] # 가로 -> 가로
        if check(i + 1, j + 1, 1): # 대각선 OK
            dp[i + 1][j + 1][1] += dp[i][j][0] # 가로 -> 대각선

        if check(i + 1, j, 2): # 세로 OK
            dp[i + 1][j][2] += dp[i][j][2] # 세로 -> 세로
        if check(i + 1, j + 1, 1): # 대각선 OK
            dp[i + 1][j + 1][1] += dp[i][j][2] # 세로 -> 대각선

        if check(i, j + 1, 0): # 가로 OK
            dp[i][j + 1][0] += dp[i][j][1] # 대각선 -> 가로
        if check(i + 1, j, 2): # 세로 OK
            dp[i + 1][j][2] += dp[i][j][1] # 대각선 -> 세로
        if check(i + 1, j + 1, 1): # 대각선 OK
            dp[i + 1][j + 1][1] += dp[i][j][1] # 대각선 -> 대각선

print(sum(dp[N][N]))