import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
print(*a, sep='\n')