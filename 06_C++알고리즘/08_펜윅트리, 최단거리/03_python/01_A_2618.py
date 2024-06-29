"""
https://www.acmicpc.net/problem/2618
백준 2618. 경찰차, P4
- N개의 동서 방향도로 (왼쪽부터 1번, 2번, ... , N번)
- N개의 남북 방향도로 (위부터 1번, 2번, ... , N번)
- 교차로 위치는 (동서 도로 번호, 남북 도로 번호)로 표시
- 두 대의 경찰차가 있음 (경찰차1, 경찰차2)
- 경찰차1은 (1, 1)에서 출발, 경찰차2는 (N, N)에서 출발
- 사건이 순서대로 주어짐
- 두 대의 경찰차의 이동거리 최소화
입력)
- 동서방향 도로의 수 N ~ [5 \ 1,000]
- 사건의 수 W ~ [1 \ 1,000]
- W줄 ~ 사건의 위치 (x, y) 
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
W = int(input())
p = [(1, 1), (N, N)] + [tuple(map(int, input().split())) for _ in range(W)]
# 경찰차1, 경찰차2의 위치  + 사건의 위치

dp = [[0 for _ in range(W + 2)] for _ in range(W + 2)]
# dp[i][j] : 경찰차1이 i번째 사건, 경찰차2가 j번째 사건에 있을 때 최소 이동거리

def dist(a, b):
    return abs(p[a][0] - p[b][0]) + abs(p[a][1] - p[b][1])

# 두 경찰차가 각각 m, n번째 사건에 있을 때 최소 이동거리
def solve(m, n):
    next = max(m, n) + 1
    if next == W + 2: return 0 # 다음 사건이 없는 경우
    if dp[m][n]: return dp[m][n] # 이미 계산한 경우
    dp[m][n] = min(
        solve(m, next) + dist(n, next),  # 경찰차2가 다음 사건으로 이동
        solve(next, n) + dist(m, next)   # 경찰차1이 다음 사건으로 이동
    )
    return dp[m][n]

print(solve(0, 1))

# dp역추적
m, n = 0, 1
for i in range(2, W + 2):
    if dp[i][n] + dist(m, i) < dp[m][i] + dist(n, i):
        # 경찰차1이 i번째 사건을 처리할때 더 이동거리가 짧은 경우
        print(1)
        m = i
    else:
        print(2)
        n = i