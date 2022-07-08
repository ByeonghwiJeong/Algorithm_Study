# 재귀 방식
# 메모이제이션 X
import sys
MOD = 10007
sys.setrecursionlimit(10 ** 7)
N, K = map(int, input().split())

def bino(n, k):
    if k == 0 or k == n:
        return 1
    return bino(n-1, k-1) + bino(n-1, k)

print(bino(N, K))