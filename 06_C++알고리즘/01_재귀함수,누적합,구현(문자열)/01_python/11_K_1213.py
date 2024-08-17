'''
https://www.acmicpc.net/problem/1213
제목 : 팰린드롬 만들기

문제
- 입력된 문자열을 이용하여 순서를 적절히 바꿔서 팰린드롬을 만들어라
- 불가능시에는 "I'm Sorry Hansoo"를 출력하라
- 정답이 여러개인 경우 사전순으로 가장 빠른 팰린드롬을 출력하라

입력
ABACABA
출력
AABCBAA
'''
import sys
from collections import Counter
input = sys.stdin.readline

S = input().strip()
counter = Counter(S)

# 홀수인 문자가 2개 이상이면 불가능
if sum(count % 2 for count in counter.values()) > 1:
    print("I'm Sorry Hansoo")
    sys.exit()

left_half = []
center = ''

for char in sorted(counter):
    count = counter[char]
    if count % 2 == 1:
        center = char
    left_half.extend(char * (count // 2))

print(''.join(left_half) + center + ''.join(reversed(left_half)))