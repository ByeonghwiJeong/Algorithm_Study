'''
https://www.acmicpc.net/problem/13144
제목 : List of Unique Numbers 

문제
- N개의 수로 이루어진 수열이 있다.
- 수열에서 연속한 부분 수열 중, 모든 수가 서로 다른 것의 개수를 구하라.

입력
- 1 : 수열의 길이 N ~ [1 \ 100,000]
- 2 : N개의 수 ~ [1 \ 100,000]
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
# dp = [0] * 100001
dp = defaultdict(int)

left = 0
right = 0
ans = 0

while right < N: # right가 N이 되면 종료
    if dp[nums[right]] == 0: # right가 가리키는 수가 처음 나온 경우
        dp[nums[right]] = 1 # dp 체크
        right += 1 # right 이동
        ans += right - left # 하단 설명 참조
    else:
        dp[nums[left]] = 0
        left += 1

print(ans)
    
'''
현재 구간이 [1, 2, 3]이고 새로운 요소 4를 추가한다고 가정
새롭게 생성되는 유니크한 부분 수열: [4], [3,4], [2,3,4], [1,2,3,4]
'''
