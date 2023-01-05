'''
< Four Squares >
- 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현
'''
N = int(input())
dp = [0] * 50001
dp[1] = 1

for i in range(2, N + 1):
    min_val = 987654321
    j = 1
    while j ** 2 <= i:
        min_val = min(min_val, dp[i - (j**2)])
        j += 1
    dp[i] = min_val + 1

print(dp[N])