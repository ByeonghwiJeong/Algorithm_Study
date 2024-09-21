'''
https://www.acmicpc.net/problem/1522
제목 : 문자열 교환

문제)
- a, b로 이루어진 문자열이 있다
- 이 문자열은 원형이므로 처음과 끝이 이어져 있다
'''

import sys
input = sys.stdin.readline

S = input().strip()
cnt_a = S.count('a')
S += S
print(min([S[i:i+cnt_a].count('b') for i in range(len(S) - cnt_a)]))

# for i in range(len(S) - cnt_a):
#     result_min = min(result_min, S[i:i+cnt_a].count('b'))

# print(result_min)