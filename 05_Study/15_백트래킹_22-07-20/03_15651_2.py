import sys
from itertools import product
from itertools import product
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]

ans = product(nums, repeat=M)

for i in ans:
    print(*i, sep=' ')

