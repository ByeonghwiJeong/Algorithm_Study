"""
https://www.acmicpc.net/problem/9935
제목: 문자열 폭발

문제)
- 문자열 & 폭발 문자열 입력
- 문자열에서 폭발 문자열이 있는 경우 폭발 문자열 제거
"""
import sys
input = sys.stdin.readline

whole_str = input().strip()
bomb_str = input().strip()
bomb_len = len(bomb_str)

stack = []
for c in whole_str:
    stack.append(c)
    if len(stack) < bomb_len:
        continue
    if not stack[-bomb_len:] == list(bomb_str):
        continue
    del stack[-bomb_len:]

if stack:
    print(*stack, sep="")
else:
    print("FRULA")