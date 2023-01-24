'''
< 볼 모으기 >
https://www.acmicpc.net/problem/17615
문제)
- Red, Blue 공 일직선
- 볼을 옮겨서 같은 색 볼끼리 인접하게 놓이도록 하려고 한다.
- 1. 옆에 다른 색깔의 볼이 있으면 그볼을 모두 JUMP
- 2. 처음 옮긴 색 고정
'''
import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
# 오른쪽 지우기
if s[-1] == 'R':
    rs = s.rstrip('R')
    a = rs.count('R')
    # b = s.count('B')
else:
    rs = s.rstrip('B')
    a = rs.count('R')
    # b = s.count('B')
if s[0] == 'R':
    ls = s.lstrip('R')
    b = ls.count('R')
else:
    ls = s.lstrip('B')
    b = ls.count('R')
    
print(min(a, len(rs)-a, b, len(ls)-b))
