'''
N x N 개의 수가 N x N 크기의 표에 채워져 있다.

1  2  3  4
2  3  4  5
3  4  5  6
4  5  6  7

1  3  6  10
3  9  16
6
10  

입력) 
    - 1 : 표의 크기 N, 구해야 하는 횟수 M
    - 2 ~ N + 1: N x N
    - M개의 x1, y1, x2, y2
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_list = []
for _ in range(N):
    _list.append(list(map(int, input().split())))

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + _list[i-1][j-1]

# for d in dp:
#     print(*d, sep=' ')

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

'''
행렬문제에서 x y에서 무엇이 행인지 열인지 확실히한다.
'''