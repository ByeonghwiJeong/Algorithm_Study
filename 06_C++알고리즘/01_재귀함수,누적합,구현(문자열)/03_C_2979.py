import sys
input = sys.stdin.readline

fare = list(map(int, input().split()))
dp = [0] * 101
for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        dp[i] += 1
result = 0
for i in dp:
    if i == 0: continue
    result += fare[i-1] * i

print(result)

