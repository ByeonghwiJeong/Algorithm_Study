'''
< 좋다 >
https://www.acmicpc.net/problem/1253
문제)
- N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면\
    그 수를 "좋다(GOOD)"고 한다.
- N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력
- 수의 위치가 다르면 값이 같아도 다른 수이다.
입력)
- 1     : 수의 개수 N ~ [1 \ 2,000]
- 2     : i번째 수를 나타내는 Ai가 N개 주어진다. ~ +- 10억
출력)
- 1     : 좋은 수의 개수
'''
import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(map(int, input().split()))

ans = 0

def two_pointer(l, target):
    global ans
    st, en = 0, len(l) - 1
    while st < en:
        s = l[st] + l[en]
        if target == s:
            ans += 1
            return
        elif target > s: st += 1
        elif target < s: en -= 1

for i in range(n):
    two_pointer(nums[:i] + nums[i+1:], nums[i])
print(ans)