from bisect import bisect_left
import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
dp = []
for i in seq:
    j = bisect_left(dp, i)
    if j == len(dp):
        dp.append(i)
    else:
        dp[j] = i
    # print(f"i:{i}, j:{j}, dp:{dp}")
print(len(dp))
"""
i:10, j:0, dp:[10]
i:20, j:1, dp:[10, 20]
i:10, j:0, dp:[10, 20]
i:30, j:2, dp:[10, 20, 30]
i:20, j:1, dp:[10, 20, 30]
i:50, j:3, dp:[10, 20, 30, 50]
"""
