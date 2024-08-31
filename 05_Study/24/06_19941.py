'''
https://www.acmicpc.net/problem/19941
제목 : 햄버거 분배

문제)
- 기다란 벤치 모양의 식탁에 햄버거와 사람이 일렬로 놓여있다.
- 햄버거는 H, 사람은 P로 표시
- 식탁의 길이 N, 햄버거를 선택할 수 있는 거리 K
- 사람과 햄버거의 위치가 주어졌을 때, 햄버거를 먹을 수 있는 사람의 최대 수

입력)
- 1		: N, K
- 2		: 'HPHPHPHP .... ' (N개의 문자열)
'''

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
table = list(input().strip())

h_q = deque()
p_q = deque()

for i, v in enumerate(table):
    if v == 'H':
        h_q.append(i)
    elif v == 'P':
        p_q.append(i)


h_index = 0
p_index = 0
h_len = len(h_q)
p_len = len(p_q)

res = 0

while h_index < h_len and p_index < p_len:
    h_pos = h_q[h_index]
    p_pos = p_q[p_index]
    dist = abs(h_pos - p_pos)
    if dist <= K:
        res += 1
        h_index += 1
        p_index += 1
    else:
        if h_pos < p_pos: # 햄버거가 더 왼쪽에 있으면
            h_index += 1
        else: # 사람이 더 왼쪽에 있으면
            p_index += 1


print(res)

