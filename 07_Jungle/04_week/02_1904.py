'''
01타일
f1 = 1
1
f2 = 2
11 00
f3
100
111
001
f1
'''
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2])%15746
print(dp[int(input())])
