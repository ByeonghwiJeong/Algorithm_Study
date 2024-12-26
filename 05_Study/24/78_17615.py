"""
https://www.acmicpc.net/problem/17615
제목: 볼 모으기

문제)
- 볼을 옮겨서 같은 색 볼끼리 인접하게 놓이도록 하려고 한다
- 규칙
    1. 바로 옆에 다른 색깔의 볼이 있으면 그 볼을 모두 뛰어 넘어 옮길 수 있다. 즉, 빨간색 볼은 옆에 있는 파란색 볼 무더기를 한 번에 뛰어 넘어 옮길 수 있다
    2. 옮길 수 있는 볼의 색깔은 한 가지이다.


바로 옆에 다른 색깔의 볼이 있으면 그 볼을 모두 뛰어 넘어 옮길 수 있다. 즉, 빨간색 볼은 옆에 있는 파란색 볼 무더기를 한 번에 뛰어 넘어 옮길 수 있다. 유사하게, 파란색 볼은 옆에 있는 빨간색 볼 무더기를 한 번에 뛰어 넘어 옮길 수 있다.
옮길 수 있는 볼의 색깔은 한 가지이다. 즉, 빨간색 볼을 처음에 옮겼으면 다음에도 빨간색 볼만 옮길 수 있다. 유사하게, 파란색 볼을 처음에 옮겼으면 다음에도 파란색 볼만 옮길 수 있다.
"""


import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

# 오른쪽에서 특정 색깔 제거 후 남은 R 또는 B의 개수 계산
if s[-1] == 'R':
    rs = s.rstrip('R')
    a_1 = rs.count('R')
    a_2 = len(rs) - a_1
else:
    rs = s.rstrip('B')
    a_1 = rs.count('R')
    a_2 = len(rs) - a_1

# 왼쪽에서 특정 색깔 제거 후 남은 R 또는 B의 개수 계산
if s[0] == 'R':
    ls = s.lstrip('R')
    b_1 = ls.count('R')
    b_2 = len(ls) - b_1
else:
    ls = s.lstrip('B')
    b_2 = ls.count('R')
    b_1 = len(ls) - b_2

print(min(a_1, a_2, b_1, b_2))