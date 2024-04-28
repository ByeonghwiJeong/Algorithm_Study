import sys
from collections import defaultdict
input = sys.stdin.readline

dp = defaultdict(int)
for _ in range(int(input())):
    l = input().rstrip()[0]
    dp[l] += 1

result = [w for w, n in dp.items() if n >= 5]
print(''.join(sorted(result)) if result else 'PREDAJA')
