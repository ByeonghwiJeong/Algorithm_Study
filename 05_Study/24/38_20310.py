'''
https://www.acmicpc.net/problem/20310
제목 : 타노스

문제
- 0과 1로 이루어진 문자열 S
- 0과 1의 개수는 각각 짝수
- S를 구성하는 문자 중 0의 절반, 1의 절반을 제거 하여 새로운 문자열 S'생성
- S'로 가능한 문자열 중 사전순으로 가장 앞서는 문자열을 출력

입력
- 1010
출력
- 01
'''

import sys
input = sys.stdin.readline

S = input().strip()

total_0 = S.count('0') // 2 
total_1 = S.count('1') // 2

# 1을 왼쪽에서부터 제거
result = []
for char in S:
    if char == '1':
        if total_1 > 0:
            total_1 -= 1
        else:
            result.append(char)
    else:
        result.append(char)

# 0을 오른쪽에서부터 제거
final_result = []
for char in reversed(result):
    if char == '0':
        if total_0 > 0:
            total_0 -= 1
        else:
            final_result.append(char)
    else:
        final_result.append(char)

print(''.join(reversed(final_result)))

