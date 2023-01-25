'''
< 빗물 >
https://www.acmicpc.net/problem/14719
문제)
- 블록 사이에 빗물이 고인다.

'''
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

# 양끝 제외하고 그 위치 기준 양쪽 높이 check
# 그 높이해서 내 높이 비교후 차감
for i in range(1, W-1):
    l = max(a[:i])
    r = max(a[i+1:])
    m = min(l, r)
    if m > a[i]: ans += m - a[i]

print(ans)