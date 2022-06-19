'''
f(n) = f(n-1) + f(n-2)
'''
MOD = 10007

dp = [0] * 1001
dp[1] = 1
dp[2] = 2
n = int(input())
for i in range(3, 1001):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD

print(dp[n])


