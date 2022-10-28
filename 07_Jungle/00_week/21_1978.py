import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * 1005
dp[0] = 0
dp[1] = 0
for i in range(2, 1001):
    if dp[i]:
        for j in range(i*2, 1001, i):
            dp[j] = 0
result = 0
for i in nums:
    if dp[i]:
        result += 1
print(result)