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
    if mix == 0:
        break
    if mix < 0: left += 1
    if mix > 0: right -= 1
print(*ans)