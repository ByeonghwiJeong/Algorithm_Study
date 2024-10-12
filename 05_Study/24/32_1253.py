'''
https://www.acmicpc.net/problem/1253
제목 : 좋다

내용)
- N개의 수 중에서 어떤 수가 다른 수 두 개의 합
    - 으로 나타낼 수 있다면 그 수를 "좋다(GOOD)"
- N개의 수가 주어지면 기중에서 좋은 수의 개수는 몇개 인지 출력
- 수의 위치가 다르면 값이 같아도 다른 수

입력)
- 1 : 수의 개수 N ~ [1 \ 2_000]
- 2 : Ai가 N개 ~ [-1_000_000_000 \ 1_000_000_000]
출력)
- 좋은 수의 개수

입력예시1)
10
1 2 3 4 5 6 7 8 9 10
출력예시1)
8
- 3,4,5,6,7,8,9,10은 좋다.
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(map(int, input().split()))

ans = 0

for i in range(N):
    target = nums[i]
    left, right = 0, N - 1

    while left < right:
        # 같은 수면 건너 뛰기
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        current_sum = nums[left] + nums[right]

        if current_sum == target:
            ans += 1
            break
        elif current_sum < target:
            left += 1
        else:
            right -= 1

print(ans)


