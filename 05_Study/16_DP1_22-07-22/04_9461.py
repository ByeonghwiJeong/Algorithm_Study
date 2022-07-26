'''
1  1  1  2  2  3  4  5  7  9
fn = fn-1 + fn-5
'''
import sys
input = sys.stdin.readline

dp = [0] * 101
N = int(input())
_init = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(1, 11):
    dp[i] = _init[i]

for i in range(11, 101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(N):
    print(dp[int(input())])