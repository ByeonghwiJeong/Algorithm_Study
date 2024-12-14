"""
https://www.acmicpc.net/problem/2631
제목: 줄세우기

문제)
- 어린이집에는 N명의 아이들이 있다 (1번부터 N번)
- 번호순서대로 일렬로 서서 걸어가도록 하였다. 이동 도중에 보니 아이들의 번호순서가 바뀌었다.
- 다시 번호 순서대로 줄을 세우기 위해서 아이들의 위치를 옮기려고 한다
- 위치를 옮기는 아이들의 수를 최소

입력)
7    : 아이들수
3
7
5
2
6
1
4
출력)
4
"""


"""
이동 횟수를 최소화하려면, 현재 줄에서 **가장 긴 증가하는 부분 수열(LIS)**을 찾고, 이를 제외한 나머지 아이들을 이동

"""

import sys
input = sys.stdin.readline

N = int(input())
children = [int(input()) for _ in range(N)]

dp = [1] * N # i번째까지의 최대 증가 수열 길이

for i in range(1, N): # i번째까지의 최대 증가 수열 길이
    for j in range(i): # i 이전의 수들과 비교
        if children[i] > children[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
