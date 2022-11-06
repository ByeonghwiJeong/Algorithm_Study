'''
< 뱀 >
https://www.acmicpc.net/problem/3190
문제)
- 뱀이 사과를 먹으면 뱀길이가 늘어난다.
- 벽또는 자기자신의 몸과 부딪히면 끝난다.
- N x N 정사각형 보드에서 진행 
- 시작 : (r, c) ~ (0 ,0)
- 뱀은 처음에 오른쪽을 향한다.
    - 뱀은 몸길이를 늘려 머리를 다음카에 위치시킨다.
    - 만약 이동한 칸에 사과가 있다면, \
        그 칸에 있던 사과는 없어지고 꼬리는 움직이지 않는다.
    - 사과가 없다면 몸길이를 줄여서 꼬리가 위치한 큰을 비워준다.
입력)
- 1     : 보드크기N~[2 \ 1000]
- 2     : 사과개수K~[0 \ 100]
- 3[K]  : 사과의 위치 >> 행,열 (1, 1)시작&&사과없음
- 4     : 뱀의 방향 변환 횟수 L ~ [1 \ 100]
- 5[L]  : L개의 줄에는 방향 변환 정보가 주어진다.
    - 정수 X와 문자 C로 이루어져 있다.
    - X초뒤에 C['L'-왼쪽, 'D'-오른쪽]
    - X는 10,000 이하의 양의 정수이며, \
        방향 전환 정보는 X가 증가하는 순으로 주어진다.
출력)
- 
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
a = [[0] * n for _ in range(n)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
# index: 0 1 2 3 (동남서북)
# L >> - 1  \\  D >> + 1
for _ in range(k):
    r1, c1 = map(int, input().split())
    a[r1 - 1][c1 - 1] = 1 # 사과 1
l = int(input())
moves = {}
for _ in range(l):
    t, d = input().split()
    moves[int(t)] = d

def turn(c_direction, d):
    if d == 'D': return (c_direction + 1) % 4
    else: return (c_direction - 1) % 4

def go(r, c):
    direction = 0
    q = deque([(r, c)])
    a[r][c] = 2 # 꼬리on
    time = 1
    while True:
        r = r + dr[direction]
        c = c + dc[direction]
        if 0 <= r < n and 0 <= c < n and a[r][c] != 2:
            if not a[r][c] == 1:  #  사과 X
                pre_r, pre_c = q.popleft()
                a[pre_r][pre_c] = 0
            a[r][c] = 2
            q.append((r, c))
            if time in moves.keys():
                direction = turn(direction, moves[time])
            time += 1
        else: return time

print(go(0, 0))

