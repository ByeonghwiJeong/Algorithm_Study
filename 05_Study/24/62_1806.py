"""
https://www.acmicpc.net/problem/1806
제목: 부분합

문제)
- 10,000이하의 자연수로 이루어진 길이 N짜리 수열이 주어짐
- 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성


입력)
10 15
5 1 3 5 10 7 4 9 2 8

출력)
2

? prefix_sum OR window_sum
"""
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

prefix_sum = [0]
for i in range(N):
    prefix_sum.append(prefix_sum[-1] + nums[i])


def find_length(target):
    st, en = 0, 1 # 왼쪽부터 시작
    result = float('inf')

    while st < N:
        current_sum = prefix_sum[en] - prefix_sum[st]
        if current_sum >= target: # S 이상이면 왼쪽을 줄임
            result = min(result, en - st)
            st += 1
        else: # S 미만
            if en < N: # 오른쪽을 늘림
                en += 1
            else: # 더 이상 늘릴 수 없으면 왼쪽을 줄임
                st += 1
    return result if result != float('inf') else 0


print(find_length(S))

