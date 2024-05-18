import sys
word = sys.stdin.readline().rstrip()
dp = [0] * 26
for s in word:
    index = ord(s) - ord('a')
    dp[index] += 1

print(*dp, sep=" ")
