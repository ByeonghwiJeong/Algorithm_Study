"""
< 게임 >
https://www.acmicpc.net/problem/1072
문제)
- 게임 횟수 X ~ 범위 10억
- 이긴 횟수 Y번
- 현재 승률 Z%
최소 K번해야 승률이 오를까?
Z가 변하지 않으면 Z
"""
import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = Y * 100 // X
l = 0
h = 10**9
sol = -1

while l <= h:
    mid = (l + h) // 2
    if (Y + mid) * 100 // (X + mid) > Z:
        sol = mid
        h = mid - 1
    else:
        l = mid + 1
print(sol)

