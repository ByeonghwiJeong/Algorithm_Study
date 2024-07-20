'''
https://www.acmicpc.net/problem/3273
제목: 두 수의 합

문제
- n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다.
- ai ~ [1 \ 1,000,000]
- 정수 x가 주어질 때, ai + aj = x를 만족하는 (ai, aj) 쌍의 개수를 구하라.

입력
- 1 : 수열의 길이 n ~ [1 \ 100,000]
- 2 : 수열 ~ [1 \ 1,000,000]
- 3 : 정수 x ~ [1 \ 2,000,000]
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(map(int, input().split()))
X = int(input())

left = 0
right = N-1
ans = 0

while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == X: # 합이 x인 경우
        ans += 1
        left += 1
        right -= 1
    elif current_sum < X: # 합이 x보다 작은 경우
        left += 1
    else: # 합이 x보다 큰 경우
        right -= 1

print(ans)