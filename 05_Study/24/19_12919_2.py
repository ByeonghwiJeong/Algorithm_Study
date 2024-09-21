'''
https://www.acmicpc.net/problem/12919
제목 : A와 B 2

문제)
- A와 B로만 이루어진 문자열 S와 T가 있다
- S를 T로 바꾸는 게임
- S에는 다음과 같은 연산을 할 수 있음
    1. 문자열 뒤에 A를 추가
    2. 문자열 뒤에 B를 추가 후 문자열 뒤집기
'''

import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

def dfs(s, t):
    if s == t:
        print(1)
        sys.exit()
    if len(s) == len(t): return
    if t[-1] == 'A':
        dfs(s, t[:-1])
    if t[0] == 'B':
        dfs(s, t[:-1][::-1])

dfs(S, T)
print(0)