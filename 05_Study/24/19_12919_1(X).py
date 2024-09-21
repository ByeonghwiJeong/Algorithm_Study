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

visited = set()  # 이미 방문한 문자열을 저장

# S에서 T 
def dfs(s):
    if s in visited:
        return
    visited.add(s)
    if s == T: 
        print(1)
        sys.exit()
    if len(s) >= len(T):  
        return
    dfs(s + 'A')
    dfs((s + 'B')[::-1])

dfs(S)
print(0)