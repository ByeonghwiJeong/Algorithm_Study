'''
피보나치 N1 = 1 N2 = 2
n = 5 ~ 40

if n = 5
f5 > f4 f3
    f4 > f3 f2
        f3> f2 f1
            f2
            f1
        f2>
    f3 > f2 f1
        f2
        f1
1 1 2 3 5
'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
dp[1] = dp[2] = 1

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N], N-2)
