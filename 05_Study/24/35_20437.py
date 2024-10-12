'''
https://www.acmicpc.net/problem/20437
제목 : 문자열 게임 2

내용)
- 새로운 문자열 게임
1. 알파벳 소문자로 이루어진 문자열 W가 주어짐
2. 양의 정수 K가 주어짐
3. 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구함
4. 어떤 문자를 정확히 K개를 포함하고, 
    문자열의 첫 번째와 마지막 글자가 문자로 같은 가장 긴 연속 문자열의 길이를 구함

같은 방식으로 게임을 T회 진행
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())): # 테스트 수
    string = input().rstrip()
    K = int(input())

    pos_dict = defaultdict(list)

    for i, char in enumerate(string):
        pos_dict[char].append(i)

    shortest = 10001  # 가장 짧은 문자열
    longest = 0       # 가장 긴 문자열

    # 각 알파벳에 대해 슬라이딩 윈도우 적용
    for index_list in pos_dict.values():
        if len(index_list) < K:
            continue

        for start in range(len(index_list) - (K - 1)):
            # start : 윈도우 시작 index
            end = start + K - 1 # 윈도우 마지막 index
            window_length = index_list[end] - index_list[start] + 1
            shortest = min(shortest, window_length)
            longest = max(longest, window_length)

    if longest == 0:
        print(-1)
    else:
        print(shortest, longest)