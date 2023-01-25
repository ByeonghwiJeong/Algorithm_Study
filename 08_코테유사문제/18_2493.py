'''
< 탑 >
https://www.acmicpc.net/problem/2493
문제)
- 일직선 위에 N개의 높익 서로 다른 탑
- 모든 탑은 순서 반대방향(왼쪽)으로 레이저 신호를 발사
'''
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stack = []
dp = [0] * n

for i, v in enumerate(a):
    while stack and a[stack[-1]] < v:
        stack.pop()
    if stack: dp[i] = stack[-1] + 1
    stack.append(i)
    
print(*dp)