'''
< 정수삼각형 >
ㅓ

00
10 11
20 21 22
30 31 32 33
40 41 42 43 44 

'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * N for _ in range(N)]
for i in range(N):
    _list = list(map(int, input().split()))
    for j in range(i+1):
        print(i, j)
        if j == 0 and i == 0:
            dp[i][j] = _list[j]
        elif j == 0:
            dp[i][j] = _list[j] + dp[i-1][0]
        elif j == i:
            dp[i][j] = _list[j] + dp[i-1][i-1]
        else:
            dp[i][j] = _list[j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))