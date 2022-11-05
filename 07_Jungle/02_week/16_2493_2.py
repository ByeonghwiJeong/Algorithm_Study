'''
코드 개선
'''
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stack = []
dp = [0] * n

for i in range(n):
    v = a[i]
    while stack and a[stack[-1]] < v:
        stack.pop()
    if stack: dp[i] = stack[-1] + 1
    stack.append(i)
print(*dp)

