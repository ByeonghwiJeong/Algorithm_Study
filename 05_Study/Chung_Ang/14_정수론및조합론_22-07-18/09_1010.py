'''
서쪽에는 N개의 사이트
동쪽에는 M개의 사이트
N <= M

'''
import sys
input = sys.stdin.readline

chk = [[0] * 31 for _ in range(31)]

def bino(n, r):
    if chk[n][r]:
        return chk[n][r]
    if n == r or r == 0:
        chk[n][r] = 1
    else:
        chk[n][r] = bino(n-1, r) + bino(n-1,r-1)
    return chk[n][r]

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(bino(M, N))
