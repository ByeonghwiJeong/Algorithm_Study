import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10 ** 7

chk = [[0] * 1001 for _ in range(1001)]

def bino(n, r):
    if chk[n][r]:
        return chk[n][r]
    if r == n or r == 0:
        chk[n][r] = 1
    else:
        chk[n][r] = bino(n-1, r) + bino(n-1, r-1)
        chk[n][r] %= 10007 
    return chk[n][r]

# for i in range(0, 1001):
#     chk[i][0] = 1
#     chk[i][i] = 1
#     for j in range(1, i):
#         chk[i][j] = chk[i-1][j] + chk[i-1][j-1]
#         chk[i][j] %= 10007

N, K = map(int, input().split())
print(bino(N, K))
