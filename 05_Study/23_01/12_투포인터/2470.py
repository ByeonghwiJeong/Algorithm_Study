'''
< 두 용액 >
https://www.acmicpc.net/problem/2470
문제)
- 용액의 특성값이 주어진다.
- 두개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들자
입력)
- 1     : 전체 용액의 수  N ~ [2 \ 100,000]
- 2     : N개의 용액의 특성 값 ~ [-10억 \ +10억]
출력)
- 1     : 
'''
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

left = 0
right = n - 1
ans = (0, 0)
_min = float('inf')

while left < right:
    mix = a[left] + a[right]
    if abs(mix) < _min:
        _min = abs(mix)
        ans = (a[left], a[right])
    if mix == 0: break
    if mix < 0: left += 1
    if mix > 0: right -= 1
print(*ans)
        




'''
정렬이 됐다고 가정하면
맨 왼쪽 가장 값은값
맨 오른쪽 가장 큰값
오른쪽으로 갈 수록 값이 커지고
왼쪽으로 갈 수록 값이 작아진다.
'''