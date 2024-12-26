"""
https://www.acmicpc.net/problem/2467
제목: 용액

문제)
- 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다
- 주어진 용액들의 특성값이 [-99, -2, -1, 4, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액의 특성값이 0에 가장 가까운 용액
- 산성 용액과 알칼리성 용액의 특성값이 정렬된 순서로 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성
"""
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

left, right = 0, N-1
ans_pair = (0, 0)
min_diff = float('inf')


while left < right:
    mix = nums[left] + nums[right]

    # 최소값 갱신
    if abs(mix) < min_diff:
        min_diff = abs(mix)
        ans_pair = (nums[left], nums[right])

    if mix == 0:
        break
    elif mix > 0:
        right -= 1
    else:
        left += 1

print(**ans_pair)