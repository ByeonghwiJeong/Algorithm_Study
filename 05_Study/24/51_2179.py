"""
https://www.acmicpc.net/problem/2179
제목 : 비슷한 단어

문제)
- N개의 영단어들이 주어졌을 때, 가장 비슷한 두 단어를 구해내는 프로그램을 작성
- 두 단어의 비슷한 정도는 두 단어의 접두사의 길이로 측정
- 즉, 두 단어의 앞에서부터 M개의 글자들이 같으면서 M이 최대인 경우
- 접두사의 길이가 최대인 경우가 여러 개일 때에는 입력되는 순서대로 제일 앞쪽에 있는 단어를 답

입력 예시 1)
9         N ~ [2, 20_000]
noon      T ~ N개의 줄에 알파벳 소문자로 이루어진 단어(100글자 이하)
is
lunch
for
most
noone
waits
until
two
출력 예시 2)
noon
noone
"""

"""
핵심아이디어 정렬수행 후 인접한 두 단어만 비교하면 됨
"""

import sys
input = sys.stdin.readline

N = int(input())
words = [(input().strip(), i) for i in range(N)]  # 단어와 입력 순서 저장
words.sort()  # 사전순 정렬

max_prefix = 0
result = None


def cnt_prefix(w1, w2):
    """두 단어의 공통 접두사 길이 계산"""
    cnt = 0
    for a, b in zip(w1, w2):
        if a == b:
            cnt += 1
        else:
            break
    return cnt

for i in 