'''
< 용액 문제 - >
https://www.acmicpc.net/problem/2110
문제)
- 산성용액 & 알칼리성용액
- 산성 ~ [1 \ 1,000,000,000]
- 알칼리 ~ [-1,000,000,000 \ -1]
- 같은 양의 두 용액 혼합시 특성값 : 각각의 특성합

- 같은 양의 두 용액을 혼합해서 0에 가까운 용액을 만들려고 한다

입력)
- 1     : 용액수 N ~ [2 \ 100,000]
- 2[N]  : 용액의 특성값들 

출력)
- 가장 인접한 두 공유기 사이의 최대 거리
'''
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))

l = 0
r = n - 1
min = float('inf')
while l < r: # 등호있으면안됨
    tot = a[l] + a[r] 
    if abs(tot) < min:
        min = abs(tot)
        ans = (a[l], a[r])
    if tot == 0: break
    elif tot < 0: l += 1
    elif tot > 0: r -= 1
print(*ans)