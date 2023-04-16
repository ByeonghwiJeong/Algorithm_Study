from bisect import bisect_left
import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
dp = []
ret = []
for i in seq:
    j = bisect_left(dp, i)
    if j == len(dp):
        dp.append(i)
        ret.append((j, i))
    else:
        dp[j] = i
        ret.append((j, i))
    # print(f"i:{i}, j:{j}, dp:{dp}")
ans = []
# print(ret)
for i in range(N - 1, -1, -1):
    if ret[i][0] == len(dp) - 1:
        ans.append(ret[i][1])
        dp.pop()

print(len(ans))
print(*ans[::-1])
